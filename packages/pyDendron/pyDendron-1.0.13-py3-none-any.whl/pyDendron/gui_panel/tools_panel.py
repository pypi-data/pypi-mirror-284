"""
Dataset tools
"""
__author__ = "Sylvain Meignier"
__copyright__ = "Copyright 2023 Sylvain Meignier, Le Mans Université, LIUM (https://lium.univ-lemans.fr/)"
__license__ = "GPL"

import pandas as pd
from pathlib import Path
import panel as pn
import param
import copy
from panel.viewable import Viewer

from pyDendron.dataset import Dataset
from pyDendron.alien.io_besancon import IOBesancon
from pyDendron.alien.io_heidelberg import IOHeidelberg
from pyDendron.alien.io_rwl import IORWL
from pyDendron.alien.sylpheIII import Sylphe
from pyDendron.tools.alignment import Alignment
from pyDendron.dataname import *
from pyDendron.gui_panel.dataset_package import DatasetPackage
from pyDendron.gui_panel.tabulator import (_cell_text_align, _cell_editors, _header_filters,
                                           _cell_formatters, _hidden_columns, unique_filename)

from pyDendron.app_logger import logger
from pyDendron.gui_panel.my_viewer import MyViewer

class ToolsPanel(MyViewer):
    """ Tools to manage dataset. """
    path = param.Foldername('./', doc='path of the data')
    filters = param.List(['*.p', '*.xlsx', '*.json'], doc='glob filter')
    encoding = param.Selector(default='utf-8', objects=['utf-8', 'latin1'], doc='')
    tolerance = param.Integer(default=5, bounds=(1, 10), step=1, doc='number of equal values tolerated')
        
    def __init__(self, dataset, parameters, dendron_info, cfg_path, **params):
        super().__init__(cfg_path, **params)
        self.dataset = dataset
        self.parameters = parameters
        self.wcolumn_selector = parameters.column.columns

        self.dataset_package = DatasetPackage(dataset, parameters.column, parameters.package, 
                                                      parameters.detrend, parameters.chronology, name='')
        self.dendron_info = dendron_info
        self.www = self.dendron_info.www
        self.import_dataset = None
        self.outliers = []
        
        self.bt_size = 90

        self._layout = pn.Tabs(
            ('Import', self._import()),
            ('Export', self._export()),
            ('Merge', self._merge()),
            ('Validate', self._validate()),
            ('Edit rings', self._edit_ring()),
            name=self.name,
             dynamic=True, styles={'font-size': '15px'})

    def get_sidebar(self, visible=True):   
        return pn.Card(pn.Param(self, show_name=False),                 
                margin=(5, 0), 
                sizing_mode='stretch_width', 
                title='Tools',
                collapsed=True, visible=visible)
  
    def get_options(self):
        """ Retrieve file options based on filters. """
        options = {}
        for flt in self.filters:
            for file in Path(self.dendron_info.dataset_path).glob(flt):
                options[f'\U0001F4E6 {str(file.name)}'] = file
        return options
    
    def _import(self):
        def get_filename():
            if self.www:
                return file_input.filename
            if len(file_input.value) == 0:
                raise ValueError('No file selected.')
            if len(file_input.value) > 1:
                logger.warning('Multiple files selected, only the first one is used.')
            return file_input.value[0]        

        def on_import(event):               
            """ Handle importing of datasets. """  
            def get_input_io():
                if file_format.value == 'Besançon':
                    return IOBesancon()
                elif file_format.value == 'Heidelberg':
                    return IOHeidelberg()
                elif file_format.value == 'RWL':
                    return IORWL()
                elif file_format.value == 'Sylphe':
                    return Sylphe()
            
            io_import = get_input_io()
            fn = get_filename()
            parent_keycode = Path(fn).stem
            if self.www:
                buffer =  file_input.value
                self.import_dataset = io_import.read_buffer(parent_keycode, buffer)
            else:
                self.import_dataset = io_import.read_file(fn)

            if self.import_dataset is not None:
                wtabulator.value = self.import_dataset.get_data()
            else:
                wtabulator.value = pd.DataFrame(columns=list(dtype_view.keys()))
        
        def on_save(event):
            """ Handle saving of the imported dataset. """
            if self.import_dataset is None:
                raise ValueError('The imported dataset is empty.')
            if dataset_name.value == '':
                raise ValueError('The dataset name is empty.')      
            fn = unique_filename(Path(self.dendron_info.dataset_path) / dataset_name.value)      
            self.import_dataset.dump(fn)
            logger.info(f'Save done in dataset {fn}')

        def on_merge(event):
            """ Handle saving of the imported dataset. """
            if self.import_dataset is None:
                raise ValueError('The imported dataset is empty.')
            if self.dataset is None:
                raise ValueError('The dataset is empty.')            
            self.dataset.append(self.import_dataset)
            logger.info('Merge done in current dataset')

        def on_file_input(event):
            fn = get_filename()
            dataset_name.value = f'dataset_{Path(fn).stem}.p'
            ch = fn.lower()
            if ch.endswith('.mdb'):
                file_format.value = 'Sylphe'
            elif ch.endswith('.fh'):
                file_format.value = 'Heidelberg'
            elif ch.endswith('.rwl') or ch.endswith('.crn'): 
                file_format.value = 'RWL'
            else:
                file_format.value = 'Besançon'
        
        """ Create the import tab layout. """

        option = ['Besançon', 'Heidelberg', 'RWL']
        if self.www:
            file_input = pn.widgets.FileInput(sizing_mode='stretch_width')  
            file_input.param.watch(on_file_input, ['filename'], onlychanged=True)
        else:
            option += ['Sylphe']
            file_input = pn.widgets.FileSelector('~', only_files=True)
            file_input.param.watch(on_file_input, ['value'], onlychanged=True)
        
        
        file_format = pn.widgets.RadioBoxGroup(name='Format', options=option, inline=True, align=('end', 'end'))
        bt_import = pn.widgets.Button(name='Import', icon='import', button_type='primary', align=('end', 'end'))
        bt_import.on_click(on_import)
        wtabulator = pn.widgets.Tabulator(
                                    pd.DataFrame(columns=list(dtype_view.keys())),
                                    hidden_columns=_hidden_columns(self.wcolumn_selector.value), 
                                    text_align=_cell_text_align(dtype_view),
                                    editors=_cell_editors(dtype_view), 
                                    header_filters=_header_filters(dtype_view), 
                                    formatters=_cell_formatters(dtype_view),
                                    sizing_mode='stretch_width',
                                    max_height=600,
                                    min_height=300,
                                    height_policy='max',
                                    )
        
        dataset_name = pn.widgets.TextInput(name='Dataset name', placeholder='dataset_import.p')
        bt_save = pn.widgets.Button(name='Create', icon='file-plus', button_type='primary', align=('start', 'end'))
        bt_save.on_click(on_save)
        bt_merge = pn.widgets.Button(name='Merge in current dataset', icon='arrow-merge', button_type='primary', align=('start', 'end'),)
        bt_merge.on_click(on_merge)
        return pn.Column(file_input,
                        pn.Row(file_format, bt_import ),
                        wtabulator,
                        pn.Row(dataset_name, bt_save),
                        bt_merge
                    )

    def _export(self):
        def on_save_dataset(event):
            if self.dataset.filename is None:
                logger.warning('Dataset is not loaded.')
                return
            fn = Path(self.dataset.filename)
            if file_export_format.value == 'Pickle':
                fn = fn.with_suffix('.p')
            elif file_export_format.value == 'JSON':
                fn = fn.with_suffix('.json')
            else:
                fn = fn.with_suffix('.xlsx')
            logger.info(f'Tools export, filename: {fn} (format {file_export_format.value})')
            self.dataset.dump(fn)
            
        def on_save_dataset_package(event):
            if self.dataset.filename is None:
                logger.warning('Dataset is not loaded.')
                return
            data = dataset_package.dt_data
            if data is None:
                logger.warning('No package to export.')
                return
            package = dataset_package.wselection.value
            if file_export_format_package.value == 'Besançon':
                bes = IOBesancon()
                fn = Path(self.path) / f'{package}.txt'
                bes.write_package(self.dataset, data, fn)
                logger.info(f'Tools export {package}, filename: {fn} (format {file_export_format_package.value})')
            elif file_export_format_package.value == 'Heidelberg':
                fh = IOHeidelberg()
                fn = Path(self.path) / f'{package}.fh'
                fh.write_package(self.dataset, data, fn)
                logger.info(f'Tools export {package}, filename: {fn} (format {file_export_format_package.value})')
            elif file_export_format_package.value == 'RWL':
                rwl = IORWL()
                fn = Path(self.path) / f'{package}.rwl'
                rwl.write_package(self.dataset, data, fn)
                logger.info(f'Tools export {package}, filename: {fn} (format {file_export_format_package.value})')
              
        file_export_format = pn.widgets.RadioBoxGroup(name='file format', options=['Pickle', 'Excel', 'JSON'], inline=True, align=('start', 'end'))
        bt_save_dataset = pn.widgets.Button(name='Save', icon='save', button_type='primary', align=('start', 'end'), width=self.bt_size)
        bt_save_dataset.on_click(on_save_dataset)
        
        file_export_format_package = pn.widgets.RadioBoxGroup(name='file format', options=['Heidelberg', 'Besançon', 'RWL'], inline=True, align=('start', 'end'))
        bt_save_dataset_package = pn.widgets.Button(name='Save', icon='save', button_type='primary', align=('start', 'end'), width=self.bt_size)
        bt_save_dataset_package.on_click(on_save_dataset_package)
        
        dataset_package = self.dataset_package
        return pn.Column(
                    pn.pane.Markdown('### Export current dataset'),
                    file_export_format,
                    bt_save_dataset,
                    pn.pane.Markdown('### Export current package'),
                    dataset_package,
                    file_export_format_package,
                    bt_save_dataset_package,
        )
  
    def _merge(self):
        """ Create the dataset merge tab layout. """
        
        def load(dataset_src_name1, dataset_src_name2):
            dataset_src = Dataset()
            dataset_src.load(dataset_src_name1.value)
            
            dataset_dest = Dataset()
            dataset_dest.load(dataset_src_name2.value)
            
            return  dataset_src, dataset_dest

        def on_merge(event):
            """ Handle merging of datasets. """
            try:
                self._layout.loading = True
                fn = unique_filename(Path(self.dendron_info.dataset_path) / dataset_dest_name.value)
                if dataset_src_name1.value == dataset_src_name2.value:
                    logger.warning('The source datasets are the same.')
                    return
                dataset_src1, dataset_src2 = load(dataset_src_name1, dataset_src_name2)
                dest = dataset_src1.clone()
                dest.filename = fn
                dest.append(dataset_src2)
                dest.dump()
                logger.info(f'Merge done into {fn}')
            except Exception as inst:
                logger.error(f'on_duplicate2 : {inst}', exc_info=True)
            finally:
                self._layout.loading = False

        options = self.get_options()
        
        dataset_src_name1 = pn.widgets.Select(name='1st dataset name', options=options)
        dataset_src_name2 = pn.widgets.Select(name='2rd dataset name', options=options)
        dataset_dest_name = pn.widgets.TextInput(value='dataset_import.p', name='Destination Dataset name')

        bt_merge = pn.widgets.Button(name='Merge', icon='arrow-merge', button_type='primary', align=('start', 'end'), width=self.bt_size)
        bt_merge.on_click(on_merge)

        return pn.Column(
                        pn.Row(dataset_src_name1, dataset_src_name2), 
                        pn.Row(dataset_dest_name, bt_merge)
                    )
        
    def _validate(self):
        """ Duplicate detection tab layout."""
        
        def on_duplicate(event):
            try:
                self._layout.loading = True
                counts = self.dataset.sequences[KEYCODE].value_counts()
                lst = list(counts[counts > 1].to_dict().keys())
                wduplicate.value =  '\n'.join(lst) if len(lst) > 0 else 'No duplicate'
            except Exception as inst:
                logger.error(f'on_duplicate2 : {inst}', exc_info=True)
            finally:
                self._layout.loading = False

        def on_duplicate2(event):
            try:
                self._layout.loading = True
                data = dataset_package.data
                if data is None:
                    logger.warning('No package.')
                    return
                res = alignment.ndiff_sequences(data, n=self.tolerance)
                txt = ''
                for idx_i, idx_j, cost , insertions, deletions, substitutions, n, err in res:
                    #idx_i, idx_j, cost , insertions, deletions, substitutions, n, ch]
                    txt += f'{err} (ins: {insertions}, del:{deletions}, sub:{substitutions})\n'
                wduplicate2.value = txt
                progress.value = 100
            except Exception as inst:
                logger.error(f'on_duplicate2 : {inst}', exc_info=True)
            finally:
                self._layout.loading = False
        
        def on_progress(event):
            progress.value = alignment.rate
            
        def on_outliers(event):
            data = dataset_package.dt_data
            txt = ''
            self.outliers.clear()
            for _, row in data.iterrows():
                vec = row[DATA_VALUES]
                idx = row[IDX_CHILD]
                med, std = np.nanmedian(vec), np.nanstd(vec)
                cut_off = std * 5 
                lower, upper = med - cut_off, med + cut_off
                keycode = row[KEYCODE]
                for i, x in enumerate(vec):
                    if (x < lower) or (x > upper) or (abs(x) <= 1e-7):
                        txt += f'Outlier {x} in "{keycode}" at index {i} (lower={round(lower, 3)}, median={round(med, 3)}, upper={round(upper, 3)})\n'
                        self.outliers.append(({IDX: idx, KEYCODE: keycode, 'Index':i, 'Value': x}))
            woutliers.value = txt

        def on_set_nan(event):
            for d in self.outliers:
                self.dataset.sequences.at[d[IDX], DATA_VALUES][d['Index']] = np.nan
            self.dataset.notify_changes('outliers')
        
        dataset_package = self.dataset_package
        bt_duplicate = pn.widgets.Button(name=f'Detect duplicate {KEYCODE}', icon='bolt', button_type='primary')
        bt_duplicate.on_click(on_duplicate)
        wduplicate = pn.widgets.TextAreaInput(name=f'Duplicate {KEYCODE}', value='', sizing_mode='stretch_width')

        alignment = Alignment()
        bt_duplicate2 = pn.widgets.Button(name=f'Detect duplicate {DATA_VALUES}', icon='bolt', button_type='primary')
        bt_duplicate2.on_click(on_duplicate2)
        progress = pn.indicators.Progress(name='Run', value=0, sizing_mode='stretch_width', disabled=True, bar_color='primary')
        alignment.param.watch(on_progress, ['rate'], onlychanged=True)
        wduplicate2 = pn.widgets.TextAreaInput(name=f'Duplicate {DATA_VALUES}', value='', sizing_mode='stretch_width')

        bt_outliers = pn.widgets.Button(name=f'Detect outliers {DATA_VALUES}', icon='bolt', button_type='primary')
        bt_outliers.on_click(on_outliers)
        woutliers = pn.widgets.TextAreaInput(name=f'Outliers {DATA_VALUES}', value='', sizing_mode='stretch_width')
        bt_set_nan = pn.widgets.Button(name='Set value to NaN', icon='bolt', button_type='primary')
        bt_set_nan.on_click(on_set_nan)

        return pn.Tabs(
            (f'Duplicate {KEYCODE}', pn.Column(bt_duplicate, wduplicate)),
            (f'Duplicate {DATA_VALUES}', pn.Column(dataset_package, pn.Row(bt_duplicate2,  progress), wduplicate2)),
            (f'Outliers {DATA_VALUES}', pn.Column(dataset_package, bt_outliers, woutliers, bt_set_nan)),
            dynamic=True
        )

    def _edit_ring(self):
        def on_insert(event):
            if len(wtabulator.selection) > 0:
                df = wtabulator.value
                i = wtabulator.selection[0]
                with warnings.catch_warnings():
                    # TODO: pandas 2.1.0 has a FutureWarning for concatenating DataFrames with Null entries
                    warnings.filterwarnings("ignore", category=FutureWarning)
                    wtabulator.value = pd.concat([df.iloc[:i], pd.DataFrame({'value' : [pd.NA]}), df.iloc[i:]]).reset_index(drop=True)
        
        def on_append(event):
            with warnings.catch_warnings():
                # TODO: pandas 2.1.0 has a FutureWarning for concatenating DataFrames with Null entries
                warnings.filterwarnings("ignore", category=FutureWarning)
                wtabulator.value = pd.concat([wtabulator.value, pd.DataFrame({'value' : [pd.NA]})]).reset_index(drop=True)

        def on_delete(event):
            if len(wtabulator.selection) > 0:
                i = wtabulator.selection[0]
                wtabulator.value = wtabulator.value.drop(i).reset_index(drop=True)
        
        def on_save(event):
            try:
                self._layout.loading = True

                idx = select.value
                array = wtabulator.value['value'].to_numpy()
                old_len = dataset_package.dataset.sequences.at[idx, DATA_LENGTH]
                length = len(array)
                data = {DATA_VALUES : array}            
                if length != old_len :
                    data[DATA_LENGTH] = length
                    data[DATE_END] = dataset_package.dataset.sequences.at[idx, DATE_BEGIN] + length
                self.dataset_package.dataset.edit_sequence(idx, data)                
                    #dataset_package.dataset.sequences.at[idx, DATA_LENGTH] = len(array)
                    #dataset_package.dataset.sequences.at[idx, DATE_END] += len(array) - old_len
                ascendants = self.dataset_package.dataset.get_ascendants(idx)
                if len(ascendants) > 0:
                    self.dataset_package.dataset.edit_sequence(ascendants, {INCONSISTENT: True})
                wtabulator.value 
            except Exception as inst:
                logger.error(f'on_save : {inst}', exc_info=True)
            finally:
                self._layout.loading = False

        def sync_data(event):
            #print('sync_data')
            options = {}
            if dataset_package.dt_data is not None :
                for i, row in dataset_package.dt_data.iterrows():
                    #print(row[KEYCODE], row[IDX_CHILD])
                    options[row[KEYCODE]] = row[IDX_CHILD]
            #print('sync_data', options)
            select.options = options

        def sync_tabulator(event):
            if select.value is not None:
                data = dataset_package.dataset.sequences.loc[select.value, DATA_VALUES]
                wtabulator.value = pd.DataFrame({'value' : data})

        dataset_package = self.dataset_package
        dataset_package.wselection.param.watch(sync_data, ['value'], onlychanged=True)
        dataset_package.panel_tabulator.visible = False
        
        select = pn.widgets.Select(name=f'Select {KEYCODE}', options=[])
        select.param.watch(sync_tabulator, ['value'], onlychanged=True)
        
        bt_insert = pn.widgets.Button(name=f'Insert', icon='insert', button_type='primary')
        bt_insert.on_click(on_insert)

        bt_append = pn.widgets.Button(name=f'Append', icon='append', button_type='primary')
        bt_append.on_click(on_append)

        bt_delete = pn.widgets.Button(name=f'Delete', icon='delete', button_type='primary')
        bt_delete.on_click(on_delete)

        bt_save = pn.widgets.Button(name=f'Save', icon='save', button_type='primary')
        bt_save.on_click(on_save)

        wtabulator = pn.widgets.Tabulator(
                                    sizing_mode='stretch_width',
                                    max_height=600,
                                    min_height=300,
                                    height_policy='max',
                                    selectable=True,
                                    show_index = True
                                    )
        
        return pn.Column(
            dataset_package,
            select,
            wtabulator,
            pn.Row(bt_insert, bt_append, bt_delete, bt_save)
        )
     
    def __panel__(self):
        """ Return the panel layout."""
        return self._layout
    



        



