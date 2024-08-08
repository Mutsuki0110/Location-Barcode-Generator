# Location Barcode Generator

This is a location barcode generator that generates a barcode image from a given string.

## Dependencies

- [code128](https://pypi.org/project/code128/)
- [Pillow](https://pypi.org/project/Pillow/)

## Usage

1. Install the dependencies
2. Run the code, follow the instructions
3. Barcode images will be saved in the `output_files` folder

## Example

```plaintext
Enter the location zone (e.g., N): N
Enter the number of digits for location number (e.g., 4): 4
Enter the start of location number: 0101
Enter the end of location number: 0428
```

## Reminder

- The location zone must be a single letter
- The location number must be a number matching the number of digits specified
- The start of the location number must be less than the end of the location number
