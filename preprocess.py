from nemo_chem.data.preprocess.preprocess import Preprocess
prep = Preprocess()
prep.prepare_dataset(
    links_file="/opt/nvidia/nemo_chem/examples/chem/conf/dataset/ZINC-downloader-test.txt",
    download_dir="/workspace/data/zinc_raw/",
    output_dir="/workspace/data/zinc_csv_split/"
)
