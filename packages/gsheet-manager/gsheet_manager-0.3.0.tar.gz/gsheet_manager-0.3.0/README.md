# GSheetManager

GSheetManager is a Python package that provides a convenient interface for managing Google Sheets. It offers features like batch updates, local caching, and automatic worksheet refreshing to optimize interactions with Google Sheets.

## Installation

You can install GSheetManager using pip:

```
pip install gsheet-manager
```

## Requirements

- Python 3.6+
- gspread library

## Usage

Here's a basic example of how to use GSheetManager:

```python
from gsheet_manager import GSheetManager

class MySheetManager(GSheetManager):
    @GSheetManager.batch_sync_with_remote
    def update_sales_data(self, product, quantity, price):
        # Find the row for the product
        product_column = 0
        quantity_column = 1
        price_column = 2
        total_column = 3

        for row, row_data in enumerate(self.local_sheet_values):
            if row_data[product_column] == product:
                # Update quantity
                self._set_buffer_cells(row, quantity_column, quantity)
                
                # Update price
                self._set_buffer_cells(row, price_column, price)
                
                # Calculate and update total
                total = quantity * price
                self._set_buffer_cells(row, total_column, total)
                
                print(f"Updated {product}: Quantity={quantity}, Price=${price}, Total=${total}")
                return

        # If product not found, add a new row
        new_row = len(self.local_sheet_values)
        self._set_buffer_cells(new_row, product_column, product)
        self._set_buffer_cells(new_row, quantity_column, quantity)
        self._set_buffer_cells(new_row, price_column, price)
        self._set_buffer_cells(new_row, total_column, quantity * price)
        print(f"Added new product {product}: Quantity={quantity}, Price=${price}, Total=${quantity * price}")

# Usage
manager = MySheetManager('path/to/key_file.json', 'Sales Sheet', 'Product Data')
manager.update_sales_data('Widget A', 100, 19.99)
manager.update_sales_data('Gadget B', 50, 24.99)
```

## Features

- Batch updates to minimize API calls
- Local caching of sheet values
- Automatic worksheet refreshing
- Decorator for syncing operations with remote

## API Reference

### GSheetManager(key_file, doc_name, sheet_name)

Creates a new GSheetManager instance.

- `key_file`: Path to your Google Service Account key file
- `doc_name`: Name of your Google Sheet
- `sheet_name`: Name of the worksheet

### Methods

- `refresh_worksheet()`: Refreshes the worksheet if the timeout has passed
- `sync_from_remote()`: Syncs local values from the remote sheet
- `batch_update_remote()`: Sends batched updates to the remote sheet
- `_set_buffer_cells(python_row_idx, python_col_idx, value)`: Sets a value in the local buffer

### Decorators

- `@batch_sync_with_remote`: Decorator for methods that need to sync with the remote sheet

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
