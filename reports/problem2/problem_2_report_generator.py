import numpy as np
import os
from datetime import date

from pylatex import *
from pylatex.utils import *

def generate_header(
    doc : any,
    todays_date : str,
    company : str = 'Georgia Institute of Technology'
) -> any:
    '''
    '''
    header = PageStyle('header')

    with header.create(Head('L')):
        header.append('Page date: ')
        header.append(LineBreak())
        header.append(todays_date)
    
    with header.create(Head('C')):
        header.append(company)

    with header.create(Head('R')):
        header.append(simple_page_number())

    doc.preamble.append(header)
    doc.change_document_style('header')

    with doc.create(MiniPage(align = 'c')):
        doc.append(LargeText(bold('HW2: Problem 2')))
        doc.append(LineBreak())
        doc.append(MediumText(bold('Ian Dover')))

    return doc

if __name__ == '__main__':
    geometry_options = {'margin': '0.7in'}
    doc = Document(geometry_options = geometry_options)

    doc = generate_header(doc, date.today())

    file_path = os.path.abspath(__file__)
    parent_directory = os.path.dirname(file_path)

    # Part A
    with doc.create(Section('Convert Image to Greyscale')):
        doc.append('Image converted to greyscale:')

        image_path = os.path.join(parent_directory, '..', '..', 'output', 'problem2', 'p2_Eagle_grayscale.jpg')

        with doc.create(Figure(position = 'h!')) as first_figure:
            first_figure.add_image(image_path, width = '120px')
            first_figure.add_caption('Greyscale image.')

    # Part 1
    with doc.create(Section('Part 1')):
        with doc.create(Subsection('Sobel Threshold: 10')):
            doc.append('Use the sobel operator on the image with a threshold of 10:')

            image_path = os.path.join(parent_directory, '..', '..', 'output', 'problem2', 'p2_part_1_sobel_thresh_10.jpg')

            with doc.create(Figure(position = 'h!')) as second_figure:
                second_figure.add_image(image_path, width = '120px')
                second_figure.add_caption('Sobel threshold of 10.')

        with doc.create(Subsection('Sobel Threshold: 50')):
            doc.append('Use the sobel operator on the image with a threshold of 50:')

            image_path = os.path.join(parent_directory, '..', '..', 'output', 'problem2', 'p2_part_1_sobel_thresh_50.jpg')

            with doc.create(Figure(position = 'h!')) as third_figure:
                third_figure.add_image(image_path, width = '120px')
                third_figure.add_caption('Sobel threshold of 50.')

        doc.append(NewPage())

        with doc.create(Subsection('Sobel Threshold: 100')):
            doc.append('Use the sobel operator on the image with a threshold of 100:')

            image_path = os.path.join(parent_directory, '..', '..', 'output', 'problem2', 'p2_part_1_sobel_thresh_100.jpg')

            with doc.create(Figure(position = 'h!')) as fourth_figure:
                fourth_figure.add_image(image_path, width = '120px')
                fourth_figure.add_caption('Sobel threshold of 100.')

        with doc.create(Subsection('Sobel Threshold: 150')):
            doc.append('Use the sobel operator on the image with a threshold of 150:')

            image_path = os.path.join(parent_directory, '..', '..', 'output', 'problem2', 'p2_part_1_sobel_thresh_150.jpg')

            with doc.create(Figure(position = 'h!')) as fifth_figure:
                fifth_figure.add_image(image_path, width = '120px')
                fifth_figure.add_caption('Sobel threshold of 150.')

        with doc.create(Subsection('Sobel Threshold: 200')):
            doc.append('Use the sobel operator on the image with a threshold of 200:')

            image_path = os.path.join(parent_directory, '..', '..', 'output', 'problem2', 'p2_part_1_sobel_thresh_200.jpg')

            with doc.create(Figure(position = 'h!')) as sixth_figure:
                sixth_figure.add_image(image_path, width = '120px')
                sixth_figure.add_caption('Sobel threshold of 200.')

        with doc.create(Subsection('Sobel Threshold: 255')):
            doc.append('Use the sobel operator on the image with a threshold of 255:')

            image_path = os.path.join(parent_directory, '..', '..', 'output', 'problem2', 'p2_part_1_sobel_thresh_255.jpg')

            with doc.create(Figure(position = 'h!')) as seventh_figure:
                seventh_figure.add_image(image_path, width = '120px')
                seventh_figure.add_caption('Sobel threshold of 255.')

        doc.append(NewPage())

    # Part 2
    with doc.create(Section('Part 2')):
        with doc.create(Subsection('Prewitt Threshold: 10')):
            doc.append('Use the prewitt operator on the image with a threshold of 10:')

            image_path = os.path.join(parent_directory, '..', '..', 'output', 'problem2', 'p2_part_2_prewitt_thresh_10.jpg')

            with doc.create(Figure(position = 'h!')) as eigth_figure:
                eigth_figure.add_image(image_path, width = '120px')
                eigth_figure.add_caption('Prewitt threshold of 10.')

        with doc.create(Subsection('Prewitt Threshold: 50')):
            doc.append('Use the prewitt operator on the image with a threshold of 50:')

            image_path = os.path.join(parent_directory, '..', '..', 'output', 'problem2', 'p2_part_2_prewitt_thresh_50.jpg')

            with doc.create(Figure(position = 'h!')) as ninth_figure:
                ninth_figure.add_image(image_path, width = '120px')
                ninth_figure.add_caption('Prewitt threshold of 50.')

        with doc.create(Subsection('Prewitt Threshold: 100')):
            doc.append('Use the prewitt operator on the image with a threshold of 100:')

            image_path = os.path.join(parent_directory, '..', '..', 'output', 'problem2', 'p2_part_2_prewitt_thresh_100.jpg')

            with doc.create(Figure(position = 'h!')) as tenth_figure:
                tenth_figure.add_image(image_path, width = '120px')
                tenth_figure.add_caption('Prewitt threshold of 100.')

        doc.append(NewPage())

        with doc.create(Subsection('Prewitt Threshold: 150')):
            doc.append('Use the prewitt operator on the image with a threshold of 150:')

            image_path = os.path.join(parent_directory, '..', '..', 'output', 'problem2', 'p2_part_2_prewitt_thresh_150.jpg')

            with doc.create(Figure(position = 'h!')) as eleventh_figure:
                eleventh_figure.add_image(image_path, width = '120px')
                eleventh_figure.add_caption('Prewitt threshold of 150.')

        with doc.create(Subsection('Prewitt Threshold: 200')):
            doc.append('Use the prewitt operator on the image with a threshold of 200:')

            image_path = os.path.join(parent_directory, '..', '..', 'output', 'problem2', 'p2_part_2_prewitt_thresh_200.jpg')

            with doc.create(Figure(position = 'h!')) as twelth_figure:
                twelth_figure.add_image(image_path, width = '120px')
                twelth_figure.add_caption('Prewitt threshold of 200.')

        with doc.create(Subsection('Prewitt Threshold: 255')):
            doc.append('Use the prewitt operator on the image with a threshold of 255:')

            image_path = os.path.join(parent_directory, '..', '..', 'output', 'problem2', 'p2_part_2_prewitt_thresh_255.jpg')

            with doc.create(Figure(position = 'h!')) as thirteenth_figure:
                thirteenth_figure.add_image(image_path, width = '120px')
                thirteenth_figure.add_caption('Prewitt threshold of 255.')

        doc.append(NewPage())

    # Part 3
    with doc.create(Section('Part 3')):
        doc.append('Detect edges using Laplacian of Gaussian:')

        image_path = os.path.join(parent_directory, '..', '..', 'output', 'problem2', 'p2_part_3_laplacian_of_gaussian.jpg')

        with doc.create(Figure(position = 'h!')) as fourteenth_figure:
            fourteenth_figure.add_image(image_path, width = '120px')
            fourteenth_figure.add_caption('Laplacian of Gaussian for edge detection.')

    # Part 4
    with doc.create(Section('Part 4')):
        doc.append('Detect edges using Difference of Gaussian:')

        image_path = os.path.join(parent_directory, '..', '..', 'output', 'problem2', 'p2_part_4_difference_of_gaussian.jpg')

        with doc.create(Figure(position = 'h!')) as fifteenth_figure:
            fifteenth_figure.add_image(image_path, width = '120px')
            fifteenth_figure.add_caption('Difference of Gaussian for edge detection.')

    doc.generate_pdf('problem2', clean_tex = False)