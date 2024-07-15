from functools import wraps
import time

import gspread
from gspread import Cell

WORKSHEET_TIMEOUT = 1800


class GSheetManager(object):
    def __init__(self, key_file, doc_name, sheet_name):
        self.key_file = key_file
        self.doc_name = doc_name
        self.sheet_name = sheet_name
        self._worksheet = self._get_worksheet()
        self._worksheet_time = time.time()
        self.buffer_cells = []
        self.local_sheet_values = []

    def _get_worksheet(self):
        gc = gspread.service_account(filename=self.key_file)
        return gc.open(self.doc_name).worksheet(self.sheet_name)

    @staticmethod
    def _instantiate_cell_object(python_row_idx, python_col_idx, value):
        return Cell(row=python_row_idx + 1,
                    col=python_col_idx + 1,
                    value=value)

    def _set_buffer_cells(self, python_row_idx, python_col_idx, value):
        for cell in self.buffer_cells:
            if (cell.row == python_row_idx + 1) and \
                    (cell.col == python_col_idx + 1):
                cell.value = value
                break
        else:
            self.buffer_cells.append(self._instantiate_cell_object(
                python_row_idx, python_col_idx, value))

    def refresh_worksheet(self):
        if time.time() - self._worksheet_time > WORKSHEET_TIMEOUT:
            self._worksheet = self._get_worksheet()
            self._worksheet_time = time.time()

    def sync_from_remote(self):
        self.local_sheet_values = self._worksheet.get_all_values()

    def batch_update_remote(self):
        if len(self.buffer_cells) == 0:
            return
        max_gsheet_row_idx = max([c.row for c in self.buffer_cells])
        max_gsheet_col_idx = max([c.col for c in self.buffer_cells])
        remote_num_rows = self._worksheet.row_count
        remote_num_cols = self._worksheet.col_count

        if max_gsheet_row_idx > remote_num_rows:
            self._worksheet.add_rows(max_gsheet_row_idx - remote_num_rows + 100)
        if max_gsheet_col_idx > remote_num_cols:
            self._worksheet.add_cols(max_gsheet_col_idx - remote_num_cols + 100)

        self._worksheet.update_cells(self.buffer_cells)
        self.buffer_cells = []

    @staticmethod
    def batch_sync_with_remote(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            self.refresh_worksheet()
            self.sync_from_remote()

            output = func(self, *args, **kwargs)

            self.refresh_worksheet()
            self.batch_update_remote()

            return output

        return wrapper
