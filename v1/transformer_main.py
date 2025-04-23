import tkinter.filedialog as fd
import os
import numpy as np
import imputer
import scaler
import encoding
import data_sm_transform as dst
from utils import file_ops
import time

class Transformer:
    def __init__(self):
        self.GREEN = '\033[32m'
        self.RESET = '\033[0m'
        self.RED = '\033[31m'

        while True:
            self.clear_screen()
            confirm = str(input(f'Press{self.GREEN} y{self.RESET} to select Dataset you want to add transformation on or{self.RED} n{self.RESET} to exit: '))
            if confirm.lower() == 'y':
                while True:
                    dataset_path_ = fd.askopenfile()
                    try:
                        self.dataset = file_ops.open_file(dataset_path_.name)
                        break
                    except AttributeError:
                        print('No pathname found. please select file from filedialog.')
                        pass
                break
            elif confirm.lower() == 'n':
                exit(0)
            else:
                print('Invalid input!')
                pass

        while True:
            self.clear_screen()
            print(f'{self.GREEN}It is recommended the transformed data should be stored in "data transformed" folder in project directory{self.RESET}')
            confirm = str(input(f'Press{self.GREEN} y{self.RESET} to select location to store transformed dataset on or{self.RED} n{self.RESET} to exit: '))
            if confirm.lower() == 'y':
                self.dt_storage = fd.askdirectory()
                if self.dt_storage == '':
                    print('Please select directory to store transformed dataset.')
                    time.sleep(1.0)
                    pass
                else:
                    break
            elif confirm.lower() == 'n':
                exit(0)
            else:
                print('Invalid input!')
                exit(1)        

    def clear_screen(self):
        os.system('cls' if os.name=='nt' else 'clear')
        
    def store_data_num(self,transformer_):
        dataset_transformed_ = transformer_.fit_transform(self.dataset)
        self.fname_ = str(input('Enter filename to save dataset as : '))
        dataset_transformed_.to_csv(f'{self.dt_storage}/{self.fname_}.csv',index=False)

    def store_data_cat(self,cname_,data_trf):
        self.fname_ = str(input('Enter filename to save dataset as : '))
        self.dataset[cname_] = data_trf
        self.dataset.to_csv(f'{self.dt_storage}/{self.fname_}.csv',index=False)

    def steps_trans(self):
        self.clear_screen()
        
        while True:
            print('Enter the integer for transformation you want to implement on the dataset :\n')
            print(f'{self.GREEN}1.[Scale] \n\n2.[Impute] \n\n3.[Encode categorical values]{self.RESET}\n')
            print(f'{self.GREEN}4.[Log/Sqrt] \n\n5.[Data binning]{self.RESET}\n\n{self.RED}6.[Exit]{self.RESET} \n\n')

            trans_type_ = int(input(': '))

            if trans_type_ in [1,2,3]:
                return trans_type_
            elif trans_type_ == 6:
                print('ended program with exit code 0')
                exit(0)
            else:
                print('Invalid input, Try Again!')
                time.sleep(1.0)
                self.clear_screen()
                pass
    
    def transformation(self):
        t_type = self.steps_trans()

        if t_type == 1:

            while True:

                self.clear_screen()
                print('Enter Scaling method :\n')
                print(f'{self.GREEN}1.[MinMax Scaling] \n\n2.[Standard Scaling] {self.RESET}\n\n')
                st_ = int(input(': '))
                if st_ == 1:
                    scaler_ = scaler.MinMaxScaler()
                    break
                elif st_ == 2:
                    scaler_ = scaler.StandardScaler()
                    break
                else: 
                    print('Invalid input, Try Again!')
                    time.sleep(1.0)
                    pass

            self.store_data_num(scaler_)


        elif t_type == 2:

            while True:

                self.clear_screen()
                print('Enter Imputing strategy :\n')
                print(f'{self.GREEN}1.[Mean] \n\n2.[Median] {self.RESET}\n\n')
                st_ = int(input(': '))
                if st_ == 1:
                    imputer_ = imputer.Imputer(stratagy='mean')
                    break
                elif st_ == 2:
                    imputer_ = imputer.Imputer(stratagy='median')
                    break
                else: 
                    print('Invalid input, Try Again!')
                    time.sleep(1.0)
                    pass

            self.store_data_num(imputer_)


        elif t_type == 3:

            while True :

                self.clear_screen()
                print('Enter Encoding method :\n')
                print(f'{self.GREEN}1.[OneHot Encoding] \n\n2.[Ordinal Encoding] {self.RESET}\n\n')
                st_ = int(input(': '))
                if st_ == 1:
                    encoder_ = encoding.Categorical_Encoder(encoding_='onehot')
                    break
                elif st_ == 2:
                    encoder_ = encoding.Categorical_Encoder(encoding_='ordinal')
                    break
                else: 
                    print('Invalid input, Try Again!')
                    time.sleep(1.0)
                    pass

            while True:

                self.clear_screen()
                print('Enter name of categorical target column (only one) :\n')
                print(self.dataset.columns)
                cname_ = str(input(': '))
                if cname_ in self.dataset.columns:
                    if self.dataset[cname_].dtype == 'object':
                        break
                else:
                    print('Invalid column, Try Again!')
                    time.sleep(1.0)
                    pass
                
            dataset_transformed_ = encoder_.fit_transform(self.dataset[cname_])
            self.store_data_cat(cname_,dataset_transformed_)

        elif t_type == 4:
            
            while True:

                self.clear_screen()
                print('Enter transform method :\n')
                print(f'{self.GREEN}This methods are strongly recommended for heavy tailed data\n')
                print(f'1.[Logarithm of column] \n\n2.[Square root of column] {self.RESET}\n\n')
                st_ = int(input(': '))

                while True:

                    self.clear_screen()
                    print('Enter name of target column (only one) :\n')
                    print(self.dataset.columns)
                    cname_ = str(input(': '))
                    if cname_ in self.dataset.columns:
                        if self.dataset[cname_].dtype != 'object':
                            break
                    else:
                        print('Invalid column, Try Again!')
                        time.sleep(1.0)
                        pass

                if st_ == 1:
                    dataset_transformed_ = dst.data_log_transform(self.dataset[cname_])
                    break
                elif st_ == 2:
                    dataset_transformed_ = dst.data_sqrt_transform(self.dataset[cname_])
                    break
                else: 
                    print('Invalid input, Try Again!')
                    time.sleep(1.0)
                    pass
            self.store_data_cat(cname_,dataset_transformed_)

        elif t_type == 5:
            
            while True:

                self.clear_screen()
                print('Enter Binning method :\n')
                print(f'1.[Normal Binning] \n\n2.[Bucketizing] {self.RESET}\n\n')
                st_ = int(input(': '))

                while True:

                    self.clear_screen()
                    print('Enter name of target column (only one) :\n')
                    print(self.dataset.columns)
                    cname_ = str(input(': '))
                    if cname_ in self.dataset.columns:
                        if self.dataset[cname_].dtype != 'object':
                            break
                    else:
                        print('Invalid column, Try Again!')
                        time.sleep(1.0)
                        pass
                
                if st_ == 1:
                    bins = [np.inf if num == 'np.inf' else float(num) for num in input('Enter bins (example : 1,2,3,4,5 , np.inf can be added.) : ').split(',')]
                    print(bins)
                    labels = [int(num) for num in input('Enter labels for bins (this should be equel to the no. of bins added) : ').split(',')]
                    print(labels)

                    try :
                        assert len(bins)-1 == len(labels)

                    except AssertionError:
                        print(f'Invalid length. got len(bins)={len(bins)}, len(labels)={len(labels)}')
                        pass

                    dataset_transformed_ = dst.bin_data(self.dataset[cname_],bins_=bins,labels_=labels)
                    break

                elif st_ == 2:
                    bins = int(input('Enter no. of bins : '))
                    labels = [int(num) for num in input('Enter labels for bins (this should be equel to the no. of bins) : ').split(',')]

                    try :
                        assert bins == len(labels)

                    except AssertionError:
                        print(f'Invalid length. got len(bins)={len(bins)}, len(labels)={len(labels)}')

                    dataset_transformed_ = dst.bucketize_data(self.dataset[cname_],n_bins_=bins,labels_=labels)
                    break
                else: 
                    print('Invalid input, Try Again!')
                    time.sleep(1.0)
                    pass
            self.store_data_cat(cname_,dataset_transformed_)

        return None

if __name__ == '__main__':
    try:
        tfr = Transformer()
        tfr.transformation()
    except KeyboardInterrupt:
        print('\n\nKeyboard Interrupted.')
        exit(1)