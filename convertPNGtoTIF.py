from osgeo import gdal
import glob
import os

src_dir = os.path.join(os.path.dirname(
    __file__), './input')
district_folder = os.listdir(src_dir)

output_dir = os.path.join(os.path.dirname(__file__), 'output')


def checkDir(dir_path):
    try:
        isDir = os.path.isdir(dir_path)
        if isDir == False:
            os.makedirs(dir_path)
            print(f'Created {dir_path} folder!')
        else:
            print(f'{dir_path} folder is exsited!')
    except Exception as e:
        return e


def run():
    try:
        global output_dir
        global district_folder
        checkDir(output_dir)
        for district in district_folder:
            if district != '.DS_Store':
                print(district)
                ward_folder = glob.glob(f'{src_dir}/{district}/*.png')
                for ward in ward_folder:
                    print(ward)
                    filename, extension = os.path.splitext(ward)
                    split = filename.split('/')
                    filename = split[len(split) - 1]

                    gdal.Translate(f'{output_dir}/{filename}.tif',
                                ward)

    except Exception as e:
        return e


run()
