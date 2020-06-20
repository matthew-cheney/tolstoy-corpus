from epub_conversion.utils import open_book, convert_epub_to_lines
import glob
from tqdm import tqdm

filenames = glob.glob('../raw_files/epub_by_work/*.epub')

for filename in tqdm(filenames):
    book = open_book(filename)
    lines = convert_epub_to_lines(book)
    split_filename = filename.split('/')
    new_filename = f'{split_filename[-1][:-5]}_markup.txt'
    with open(f'../working_files/{new_filename}', 'w') as f:
        for line in lines:
            print(line, file=f)
