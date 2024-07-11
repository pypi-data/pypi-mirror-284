"""
Crossdating tools
"""
__license__ = "GPL"
__author__ = "Sylvain Meignier"
__copyright__ = "Copyright 2023 Sylvain Meignier, Le Mans Université, LIUM (https://lium.univ-lemans.fr/)"

import logging
import pandas as pd
import matplotlib
matplotlib.use('Agg')

import panel as pn
import json
import param
import time
import numpy as np
import warnings

from panel.viewable import Viewer
from bokeh.io import export_svgs, export_svg
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
from bokeh.palettes import Category10
from pathlib import Path
from io import BytesIO

from pyDendron.app_logger import logger#, notification_stream_handler, notification_level
from pyDendron.dataname import *
from pyDendron.crossdating import CrossDating, COLS
from pyDendron.gui_panel.dataset_package import DatasetPackage

from pyDendron.gui_panel.tabulator import (_cell_text_align, _cell_editors, _header_filters_lookup,
                                           _cell_formatters, _hidden_columns, _get_selection,
                                             get_download_folder, unique_filename)

class CrossDatingPanel(Viewer):
    """A panel for cross-dating analysis.

    This panel provides functionality for cross-dating analysis, including filtering, visualization, and exporting of results.

    Parameters:
    - dataset (Dataset): The dataset for cross-dating analysis.
    - parameters (Parameters): The parameters for cross-dating analysis.
    - cfg_path (str): The path to the configuration file.

    Attributes:
    - inner (bool): Flag indicating whether inner cross-dating is enabled.
    - param_array (ParamArray): Parameters related to the array crossdating.
    - param_filter (ParamFilter): Parameters related to filtering of results.
    - cfg_file (str): The path to the configuration file.
    - results (None or DataFrame): The computed results of cross-dating analysis.
    - pmatrix (None or Matplotlib Figure): The matrix plot of cross-dating analysis.
    - pstem (None or Bokeh Figure): The stem plot of cross-dating analysis.
    - gplot (None or Bokeh Figure): The graph plot of cross-dating analysis.
    - dataset_package (DatasetPackage): The dataset package for cross-dating analysis.
    - master_dataset_package (DatasetPackage): The master dataset package for cross-dating analysis.
    - stop_thread (bool): Flag indicating whether the analysis thread should be stopped.
    - dt_param (None or Parameters): The parameters for date transformation.
    - cross_dating (CrossDating): The cross-dating object.
    - wtabulator (Tabulator): The tabulator widget for displaying results.
    - plot (None or Plot): The plot widget for displaying the selected result.
    - wrun (Row): The row widget containing the run buttons.
    - warray (Column): The column widget containing the array-related widgets.
    - wheat_matrix (Matplotlib): The Matplotlib widget for displaying the matrix plot.
    - wstem (Bokeh): The Bokeh widget for displaying the stem plot.
    - wzstem (Bokeh): The Bokeh widget for displaying the zoomed stem plot.
    - whist (Column): The column widget for displaying the histogram plot.
    - wmap (Bokeh): The Bokeh widget for displaying the map plot.
    - wgraph (Bokeh): The Bokeh widget for displaying the graph plot.
    - tabs (Tabs): The tabs widget for switching between different views.

    Methods:
    - get_tabulator(): Returns the Tabulator widget for displaying results.
    - _sync_data(event): Synchronizes the data when the dataset package changes.
    - get_plot(row): Returns the plot widget for the selected result.

    """

    inner =  param.Boolean(True, doc='Inner crossdation')

    class ParamArray(param.Parameterized):
        max_results = param.Integer(default=500000, allow_None=True, bounds=(100000, 3000000), step=100000, doc='Maximum number of results displayed')
        group_by = param.Selector(default=None, objects=[None, DATE_END_ESTIMATED, DATED, T_RANK, Z_RANK, D_RANK], doc='group scores by column')
        columns = param.ListSelector(default=list(set(list(CrossDating.COLS.keys()))- set([IDX, IDX_MASTER])), 
                                objects=list(CrossDating.COLS.keys()),
                                doc='array crossdating columns')
    param_array = ParamArray(name='Array')
    
    class ParamFilter(param.Parameterized):
        score = param.Selector(default=T_SCORE, objects=[T_SCORE, Z_SCORE, DIST], doc='score applyed with threshold')
        filter_threshold = param.Boolean(False, doc='apply filter using score threshold')
        threshold = param.Number(default=0, allow_None=True, bounds=(None, None), step=0.5, doc='Keep results upper the threshold')
        filter_max_rank = param.Boolean(True, doc='apply filter using rank value')
        max_rank = param.Integer(default=10, allow_None=True, bounds=(1, None), step=1, doc='Keep top ranking results based on score field')
        filter_dated = param.Boolean(False, doc=f'apply filter on {DATED}')
        dated = param.Boolean(True, doc='apply filter using rank value')
    param_filter = ParamFilter()


    def __init__(self, dataset, parameters, cfg_path, **params):
        super(CrossDatingPanel, self).__init__(**params)   
        self.cfg_file = cfg_path / Path(f'{self.__class__.__name__}.cfg.json')

        bt_size = 75
        self.results = None
        self.pmatrix = None
        self.pstem = None
        self.gplot = None
        self.dataset_package = DatasetPackage(dataset, parameters.column, parameters.package, 
                                                      parameters.detrend, parameters.chronology, name='hyp')
        self.master_dataset_package = DatasetPackage(dataset, parameters.column, parameters.package, 
                                                      parameters.detrend, parameters.chronology, name='master')
        self.master_dataset_package._layout.visible = False
        self.stop_thread = False

        self.dataset_package.param.watch(self._sync_data, ['notify_package_change'], onlychanged=True)
        self.master_dataset_package.param.watch(self._sync_data, ['notify_package_change'], onlychanged=True)

        self.dt_param = None

        self.cross_dating = self.load_cfg()

        row_dataset_view = pn.Row(self.dataset_package, pn.pane.HTML('<span> </span>'), self.master_dataset_package,
                margin=(5, 0), sizing_mode='stretch_width')

        self.bt_compute = pn.widgets.Button(name='Run', icon='sum', button_type='primary', align=('start', 'center'), width=bt_size)
        self.bt_compute.on_click(self.on_compute)
        self.bt_stop = pn.widgets.Button(name='Stop', icon='stop', button_type='primary', align=('start', 'center'), width=bt_size)
        self.bt_stop.on_click(self.on_stop)
        self.bt_compute.disabled = False
        self.bt_stop.disabled = True

        self.progress = pn.indicators.Progress(name='Run', value=0, width=400, disabled=True, bar_color='primary')
        self.progress_info = pn.pane.HTML()
        self.cross_dating.progress.param.watch(self.on_progress, ['count'], onlychanged=True)

        self.bt_dated = pn.widgets.Button(name='Dated / Undated', icon='swicth', button_type='primary', align=('start', 'center'), width=2*bt_size)
        self.bt_dated.on_click(self.on_dated)
        
        self.bt_export = pn.widgets.FileDownload(callback=self.on_export, filename='crossdating.xlsx', embed=False, 
                                                label='Download Excel', icon='file-export', button_type='primary', 
                                                width=2*bt_size, align=('start', 'end'))


        self.param_array.param.watch(self.on_group_by, ['group_by'], onlychanged=True)
        self.param_array.param.watch(self.on_columns, ['columns'], onlychanged=True)
        self.param_filter.param.watch(self.on_tabs, ['score', 'filter_threshold', 'threshold', 'filter_max_rank', 'max_rank', 'filter_dated', 'dated'], onlychanged=True)
        
        self.cross_dating.param_matrix.param.watch(self.on_tabs, ['size_scale', 'font_scale',  'method', 'metric', 'sorted'], onlychanged=True)
        self.cross_dating.param_stem.param.watch(self.on_tabs, ['keycode_nrows', 'height', 'window_size'], onlychanged=True)
        self.cross_dating.param_hist.param.watch(self.on_tabs, ['bullet_size', 'font_size', 'aspect', 'height'], onlychanged=True)
        self.cross_dating.param_graph.param.watch(self.on_tabs, [ 'height', 'font_size', 'line_ratio', 'bullet_ratio'], onlychanged=True)

        self.cross_dating.param_map.param.watch(self.on_tabs, ['label_distance', 'alpha', 'map_type', 'map_radius', 'map_center','line_ratio', 'height', 'font_size', 'bullet_ratio'], onlychanged=True)

        self.col = self.columns()

        self.wtabulator = self.get_tabulator()
        self.plot = None
        self.wrun = pn.Row(
                        self.bt_compute,
                        pn.Column(
                            self.progress_info,
                            self.progress,
                            ),
                        self.bt_stop
                    )

        self.warray = pn.Column(pn.Row(self.bt_dated, self.bt_export), 
                                self.wtabulator)
        self.wheat_matrix = pn.pane.Matplotlib()
        self.wstem = pn.pane.Bokeh()
        self.wzstem = pn.pane.Bokeh()
        self.whist = pn.Column()
        self.wmap = pn.pane.Bokeh()
        self.wgraph = pn.pane.Bokeh()
        
        #self.bt_svg = pn.widgets.Button(name='Save plot', icon='svg', button_type='primary', align=('start', 'end'), width=2*bt_size)
        #self.bt_svg.on_click(self.on_save_svg)

        self.tabs = pn.Tabs(('Array', self.warray),
                           ('Matrix', pn.Column('Computed only on dated *scores*. Threshold filter allowed.', self.wheat_matrix)), 
                           ('Timeline', pn.Column('Computed on all *scores*. Threshold and rank filters allowed.', self.wstem, self.wzstem, sizing_mode='stretch_width')), 
                           ('Density', pn.Column('Computed on all *scores*. Threshold and rank are disallowed.', self.whist)),
                           ('Map', pn.Column('Computed only on dated *scores*. Threshold filter allowed.', self.wmap)),
                           ('Graph', pn.Column('Computed only on dated *scores*. Threshold filter allowed.', self.wgraph)),
                           dynamic=False)
        self.tabs.param.watch(self.on_tabs,  ['active'], onlychanged=True)

        self._layout = pn.Column(
                row_dataset_view, 
                self.wrun,
                self.tabs,
                name=self.name,
                margin=(5, 0), sizing_mode='stretch_width')

    def get_tabulator(self):
        """
        Returns a Tabulator widget populated with data.

        Returns:
            pn.widgets.Tabulator: A Tabulator widget.
        """
        dtype_columns = self.dtype_columns()

        return pn.widgets.Tabulator(pd.DataFrame(columns=self.col),
                                    hidden_columns=['index', IDX_MASTER, IDX], #_hidden_columns(dtype_view=col), 
                                    text_align=_cell_text_align(dtype_columns),
                                    editors=_cell_editors(dtype_columns, False),
                                    header_filters=_header_filters_lookup(dtype_columns),
                                    formatters=_cell_formatters(dtype_columns),
                                    pagination='local',
                                    page_size=100000,
                                    frozen_columns=[KEYCODE, KEYCODE_MASTER],
                                    selectable='checkbox', 
                                    sizing_mode='stretch_width',
                                    layout='fit_data_fill',
                                    height_policy='max',
                                    max_height=500,
                                    min_height=400,
                                    show_index = False,
                                    row_content = self.get_plot,
                                    )
    
    def _sync_data(self, event):
        self.clean()

    def get_plot(self, row):
        """
        Generates a plot based on the given row data.

        Parameters:
            row (pandas.Series): The row data containing information for generating the plot.

        Returns:
            pn.pane.Bokeh: The generated plot as a Bokeh pane.

        Raises:
            None

        """
        try:
            data = self.dataset_package.data.loc[self.dataset_package.data[IDX_CHILD] == row[IDX], DATA_VALUES].iloc[0]
            if not self.inner:
                data_master = self.master_dataset_package.data.loc[self.master_dataset_package.data[IDX_CHILD]  == row[IDX_MASTER], DATA_VALUES].iloc[0] 
            else:
                data_master = self.dataset_package.data.loc[self.dataset_package.data[IDX_CHILD]  == row[IDX_MASTER], DATA_VALUES].iloc[0]
            offset = row[OFFSET]
            ds = ColumnDataSource()
            ds_master = ColumnDataSource()
            ds.data['x'] =  np.arange(len(data)) + offset
            ds.data['y'] =  data
            ds_master.data['x'] = np.arange(len(data_master))
            ds_master.data['y'] = data_master
            fig = figure(margin=(5), toolbar_location="below", height=200, width=1000,
                    tools="pan,wheel_zoom,box_zoom,reset,hover,crosshair", 
                    tooltips=[('(date/offset,value)', '(@x, @y)')],
                    sizing_mode='stretch_width')
            fig.line('x', 'y', source=ds, line_width=1, line_color=Category10[10][0], legend_label='serie')
            fig.line('x', 'y', source=ds_master, line_width=1, line_color=Category10[10][1], legend_label='master')
            #fig.varea(x="x", y1=breed, y2=0, source=source, fill_alpha=0.3, fill_color=color)
            #twin axe https://docs.bokeh.org/en/latest/docs/examples/basic/axes/twin_axes.html
            self.plot = pn.pane.Bokeh(fig, sizing_mode='stretch_width')
        except Exception:
            self.plot = None
        finally:
            return self.plot
        
    def update_col(self):
        col = self.columns()
        dtype_columns = self.dtype_columns()
        self.param_array.param.columns.objects = col
        self.param_array.columns = list(set(col)- set([IDX, IDX_MASTER]))
        self.wtabulator.hidden_columns=_hidden_columns(columnList=col, dtype_view=dtype_columns) 
        self.wtabulator.text_align=_cell_text_align(dtype_columns)
        self.wtabulator.editors=_cell_editors(dtype_columns, False)
        self.wtabulator.header_filters=_header_filters_lookup(dtype_columns)
        self.wtabulator.formatters=_cell_formatters(dtype_columns)

    def on_export(self):
        try:
            if (self.wtabulator.value is None) or (len(self.wtabulator.value) <=0 ):
                logger.warning('No data')
                return     
            output = BytesIO()
            with pd.ExcelWriter(output) as writer:
                data = self.wtabulator.value
                data.to_excel(writer, sheet_name='crossdating', merge_cells=False, float_format="%.6f")
            output.seek(0)
            return output

        except Exception as inst:
            logger.error(f'on_excel: {inst}', exc_info=True)

    def on_columns(self, event):
        self.wtabulator.hidden_columns=_hidden_columns(columnList=self.param_array.columns, 
                                                       dtype_view=self.dtype_columns()) 

    def on_group_by(self, event):
        if self.param_array.group_by is None:
            self.wtabulator.groupby = []
        else:
            self.wtabulator.groupby = [self.param_array.group_by]

    def on_tabs(self, event):
        def get_filter(threshold, rank, dated):
            param = {}
            param['score'] = self.param_filter.score
            if self.param_filter.filter_threshold and threshold:
                param['threshold'] = self.param_filter.threshold
            if self.param_filter.filter_max_rank and rank:
                param['max_rank'] = self.param_filter.max_rank
            if self.param_filter.filter_dated and dated:
                param['dated'] = self.param_filter.dated
            return param
        
        def concat_data():
            dt_data = self.dataset_package.data
            dt_data_master = self.master_dataset_package.data 
            if self.inner is None:
                return dt_data
            else:
                if (dt_data is None) and (dt_data_master is None):
                    return None
                with warnings.catch_warnings():
                    # TODO: pandas 2.1.0 has a FutureWarning for concatenating DataFrames with Null entries
                    warnings.filterwarnings("ignore", category=FutureWarning)
                    return pd.concat([dt_data, dt_data_master ], ignore_index=True)

        try:
            MAX_VALUES = 5000000
            self._layout.loading = True
            if len(self.cross_dating.results) <= 0:
                #logging.warning(f'No results to display.')
                return 
            if self.tabs.active == 0: #Array
                #logger.info(f'set_tabulator concat {self.wtabulator.pagination} {self.wtabulator.page_size} {time.time()}')
                self.wtabulator.value = pd.DataFrame(columns=self.col)
                p = get_filter(True, True, True)
                #print('on_tabs', p)
                df = self.cross_dating.concat_results(**p)
                #logger.info(f'set_tabulator concat {len(df)}, {time.time()}')
                if len(df) < self.param_array.max_results:
                    self.wtabulator.value = df
                else:
                    logging.warning(f'Too many results, the displayed array will be limited to {self.param_array.max_results/1000000}M of values.')
                    self.wtabulator.value = df.sort_values(by=self.param_filter.score).iloc[ :self.param_array.max_results]
                #logger.info(f'set_tabulator end {len(df)}, {time.time()}')
            elif self.tabs.active == 1: #Matrix
                self.wheat_matrix.object = self.cross_dating.heat_matrix(**get_filter(True, False, False), 
                                            metric=self.cross_dating.param_matrix.metric, method=self.cross_dating.param_matrix.method)
            elif self.tabs.active == 2: #Time line
                self.wstem.object, self.wzstem.object = self.cross_dating.stem(**get_filter(True, True, False))
            elif self.tabs.active == 3: 
                self.whist.clear()
                self.figs, self.gplot_cols = self.cross_dating.hist(score=self.param_filter.score)
                #self.whist.append(gp)
                self.whist.append(self.gplot_cols)
            elif self.tabs.active == 4: 
                self.wmap.object = self.cross_dating.map( **get_filter(True, True, False), data_dt=concat_data())
            elif self.tabs.active == 5: 
                self.wgraph.object = self.cross_dating.graph( **get_filter(True, True, False))
        except Exception as inst:
            logger.error(f'CrossDating: {inst}', exc_info=True)
            self.wtabulator.value = pd.DataFrame(columns=self.col)
            self.wheat_matrix.object = None
            self.wstem.object = None
            self.whist.objects = None
        finally:
            self._layout.loading = False

    @param.depends("inner", watch=True)
    def _update_inner(self):
        if self.inner == True :
            self.master_dataset_package._layout.visible = False
        else:
            self.master_dataset_package._layout.visible = True

    def get_sidebar(self, visible=True):
        self.p_panel = pn.Param(self.param, show_name=False)
        self.p_filter = pn.Param(self.param_filter, show_name=True)
        self.p_cross = pn.Param(self.cross_dating, show_name=False)
        self.parray = pn.Param(self.param_array, show_name=False)
        self.pmatrix = pn.Param(self.cross_dating.param_matrix, show_name=False)
        self.pstem = pn.Param(self.cross_dating.param_stem, show_name=False)
        self.phist = pn.Param(self.cross_dating.param_hist, show_name=False)
        self.pmap = pn.Param(self.cross_dating.param_map, show_name=False)
        self.pgraph = pn.Param(self.cross_dating.param_graph, show_name=False)
        
        return pn.Card(self.p_panel, self.p_cross, self.p_filter, 
                       pn.Tabs(self.parray, self.pmatrix, self.pstem, self.phist),
                       pn.Tabs(self.pmap, self.pgraph),
                title='Crossdating', sizing_mode='stretch_width', margin=(5, 0), collapsed=True, visible=visible)  

    def dump_cfg(self):
        with open(self.cfg_file, 'w') as fd:
            data = {
                'param' : self.param.serialize_parameters(),
                'param_filter' : self.param_filter.param.serialize_parameters(),
                'param_array' : self.param_array.param.serialize_parameters(),
                'cross_dating' : self.cross_dating.param.serialize_parameters(),
                'cross_dating.param_matrix' : self.cross_dating.param_matrix.param.serialize_parameters(),
                'cross_dating.param_stem' : self.cross_dating.param_stem.param.serialize_parameters(),
                'cross_dating.param_hist' : self.cross_dating.param_hist.param.serialize_parameters(),
                'cross_dating.param_map' : self.cross_dating.param_map.param.serialize_parameters(),
                'cross_dating.param_graph' : self.cross_dating.param_graph.param.serialize_parameters(),
            }
            json.dump(data, fd)

    def load_cfg(self):
        cross_dating = CrossDating()
        try:
            if Path(self.cfg_file).is_file():
                with open(self.cfg_file, 'r') as fd:
                    data = json.load(fd)
                    self.param_filter = self.ParamFilter(**self.ParamFilter.param.deserialize_parameters(data['param_filter']))
                    self.param_array = self.ParamArray(**self.ParamArray.param.deserialize_parameters(data['param_array']))
                    cross_dating = CrossDating(**CrossDating.param.deserialize_parameters(data['cross_dating']))
                    cross_dating.param_matrix = CrossDating.ParamMatrix(** CrossDating.ParamMatrix.param.deserialize_parameters(data['cross_dating.param_matrix']))
                    cross_dating.param_stem =  CrossDating.ParamStem(** CrossDating.ParamStem.param.deserialize_parameters(data['cross_dating.param_stem']))
                    cross_dating.param_hist =  CrossDating.ParamHist(** CrossDating.ParamHist.param.deserialize_parameters(data['cross_dating.param_hist']))
                    cross_dating.param_map =  CrossDating.ParamMap(** CrossDating.ParamMap.param.deserialize_parameters(data['cross_dating.param_map']))
                    cross_dating.param_graph =  CrossDating.ParamGraph(** CrossDating.ParamGraph.param.deserialize_parameters(data['cross_dating.param_graph']))
                    print(json.loads(data['param']))
                    for key, value in json.loads(data['param']).items():
                        if key in self.param.params().keys():
                            if key != 'name':
                                #print(f'crossdating load_cfg: set {key} = {value}')
                                self.param.set_param(key, value)
        except Exception as inst:
            logger.warning(f'ignore cfg crossdating panel, version change.')
            logger.error(f'crossdating load_cfg: {inst}')
        finally:
            #print(cross_dating)
            return cross_dating

    def columns(self):
        return list(CrossDating.COLS.keys())

    def dtype_columns(self):
        return CrossDating.COLS
        
    def __panel__(self):
        return self._layout

    def get_selection(self) -> pd.DataFrame:
        """
        Returns the view of selectionned series. 
        """
        return _get_selection(self.wtabulator)
    
    def on_link(self, event):
        if not self.inner:
            raise ValueError('Only available for self crossdating (inner parameter must be True)')
        selections = self.get_selection()
        logger.warning('link selection is not implemented yet')
        
    def on_dated(self, event):
        selections = self.get_selection()
        df = self.wtabulator.value.copy()        
        dated = selections.loc[selections[DATED] == True]
        if len(dated) > 0:
            logger.warning('dated pairs are ignored')
        undated = selections.loc[selections[DATED] == False]
        for (idx, idx_master), grp in undated.groupby([IDX, IDX_MASTER]):
            #print('groupby', idx, idx_master, len(grp))
            if len(grp) > 1:
                logger.warning('multipled undated pairs are ignored')
            else:        
                mask = (df[IDX] == idx) & (df[IDX_MASTER] == idx_master)
                df.loc[mask, DATED] = False
                df.loc[grp.index[0] , DATED] = True
                date_begin = df.loc[grp.index[0] , DATE_BEGIN_ESTIMATED]
                self.dataset_package.dataset.set_dates(idx, date_begin, warning=False)
                ascendants = self.dataset_package.dataset.get_ascendants(idx)
                if len(ascendants) > 0:
                    self.dataset_package.dataset.edit_sequence(ascendants, INCONSISTENT, True)
                
                d = df.loc[grp.index[0] ].to_dict()
                d.update(self.dt_param)
                self.dataset_package.dataset.log_crossdating(d)
                self.dataset_package.sync_data(event)
        
        self.dataset_package.dataset.notify_changes('save')
        self.wtabulator.value = df

    def on_stop(self, event):
        logger.info('on_stop')

    def clean(self):
        self.plot = None
        self.results = None
        self.wtabulator = self.get_tabulator()
        self.warray[-1] = self.wtabulator
        self.wheat_matrix.object = None
        self.wstem.object = None
        self.wzstem.object = None
        self.whist.object = None
        self.wmap.object = None
        self.wgraph.object = None
        self.dt_param = None

    def on_compute(self, event):
        if self.dataset_package.dt_data is None:
            logger.warning('No data to process.')
            return
        try:
            self.bt_compute.disabled = True
            self.bt_stop.disabled = False
            dt_data = self.dataset_package.dt_data
            dt_data_master = self.master_dataset_package.dt_data if not self.inner else None
            self.dt_param = self.dataset_package.dt_param
            if (not self.inner) and (self.dt_param != self.master_dataset_package.dt_param):
                raise ValueError('master and dataset parameters are not equal')
            
            self.progress_info.object = f'<span>start running...</span>'
            self.results = self.cross_dating.run(dt_data, dt_data_master, self.dt_param)
            
            name = 'crossdating_' + self.dataset_package.get_package_name() 
            if not self.inner:
                name += '_' + self.master_dataset_package.get_package_name()
            self.bt_export.filename = name + '.xlsx'
            
            self.on_tabs(None)
        except Exception as inst:
            logger.error(f'on_compute: {inst}', exc_info=True)
            self.clean()
        finally:
            rate, info = self.cross_dating.progress.info() 
            self.progress_info.object = f'<span>{info}</span>'
            self.progress.value = rate
            self.update_col()
            self.bt_compute.disabled = False
            self.bt_stop.disabled = True

    # def on_save_svg(self, event):
    #     try:           
    #         if self.figs is not None:
    #             for fig in self.figs:
    #                 fig.output_backend = 'svg'
    #                 export_svgs(fig, filename="plotHist.svg")
    #                 break
    #     except Exception as inst:
    #         logger.error(f'on_save_svg: {inst}', exc_info=True)

    def on_progress(self, event):
        if self.cross_dating.progress.count == self.cross_dating.progress.max_count:
            self.progress.disabled = True
            return
        self.progress.disabled = False
        rate, info = self.cross_dating.progress.info() 
        self.progress.value = rate
        self.progress_info.object = f'<span>{info}</span>'
        