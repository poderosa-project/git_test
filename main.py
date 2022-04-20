from data.medicaldata import MedicalType
from transform import Transformer
import argparse
import warnings
def fxn():
    warnings.warn("deprecated", DeprecationWarning)

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    fxn()

def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'y', 'true', '1'):
        return True
    if v.lower() in ('no','n','false', '0'):
        return False
    # Default Value
    return False

parser = argparse.ArgumentParser("Medical Data Transformer")
parser.add_argument('--base_path',help="Define Your Base Path", required=True, default="")
parser.add_argument('--src_domain', help="Define Your Source Domain [expected string: NECT, CECT, MRI_T1, MRI_T2, MRI_GD, MRI_GD_F, MRI_GD_T, MRI_ADC, MRI_DWI,T1CE]", required=True, default='CT')
parser.add_argument('--target_domain', help="Define Your Target Domain [expected string: NECT, CECT, MRI_T1, MRI_T2,MRI_GD, MRI_GD_F, MRI_GD_T, MRI_ADC, MRI_DWI,T1CE]", required=True, default="MRI_T1")
parser.add_argument('--window_width', help="Choose whether reflect window width and window level or no reflect", default=True, required=False, type=str2bool)
parser.add_argument('--is_ct_fixed', help="Define is ct fixed when you slice matching your medical image data",default=False, required=False, type=str2bool)
parser.add_argument('--is_spine',help="Define Current Process on Brain or Spine", default=False, required=False, type=str2bool)
parser.add_argument('--prefix', help='Define file prefix', default="", required=False)
parser.add_argument('--is_topbottom', help='If you need slice selection, insert an Excel file containing information', default="", required=False)
# parser.add_argument('--except_list', help='subject number list to be excluded', default="", required=False)
# parser.add_argument("--except_patient", help="If you want to except patient from all patient list, input patient list that you want to except", required=False, default="")
args = parser.parse_args()

medical_type_map = {
    'CT' : MedicalType.CT,
    'MRI_T1' : MedicalType.MRI,
    'MRI_T2' : MedicalType.T2,
    'NECT' : MedicalType.NECT,  # non-enhanced CT
    'CECT' : MedicalType.CECT,
    'MRI_GD' : MedicalType.GD,
    'MRI_GD_F': MedicalType.GD_F,
    'MRI_GD_T': MedicalType.GD_T,
    'MRI_ADC': MedicalType.ADC,
    'DWI_b0': MedicalType.DWI_b0,
    'DWI_b1000': MedicalType.DWI_b1000,
    'PORTAL': MedicalType.PORTAL,
    "T1CE" : MedicalType.T1CE,
    "FLAIR" : MedicalType.FLAIR
}

if __name__ == '__main__':
    # base_path = args.base_path if args.base_path is not "" else "/data/teamelysium/temp_data" # annotated by nestory
    base_path = args.base_path if args.base_path is not "" else "/data/teamelysium/brain/Catholic"
    print('done')
    src_type = medical_type_map[args.src_domain]
    prefix = args.prefix
    target_type = medical_type_map[args.target_domain]
    is_window = args.window_width

    assert type(is_window) == bool
    is_ct_fixed = args.is_ct_fixed

    assert type(is_ct_fixed) == bool

    is_spine = args.is_spine

    print('transformer start')
    # transformer = Transformer(src_type, target_type, base_data_path=base_path, prefix=prefix, is_window=is_window, is_ct_fixed=is_ct_fixed,is_spine=is_spine)
    transformer = Transformer(src_type, target_type, base_data_path=base_path, prefix=prefix, is_window=is_window, is_ct_fixed=is_ct_fixed,is_spine=is_spine)
    transformer.transform()
