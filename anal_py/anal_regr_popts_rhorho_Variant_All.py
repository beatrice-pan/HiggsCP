import numpy as np
from glob import glob
import os, errno

import matplotlib.pyplot as plt

from anal_utils import calculate_metrics_regr_popts

filelist_rhorho_Variant_All=[]
filelist_rhorho_Variant_All.append('npy/nn_rhorho_Variant-All_regr_popts_Unweighted_False_NO_NUM_CLASSES_0/monit_npy/')


metrics_Variant_All = [calculate_metrics_regr_popts(filelist_rhorho_Variant_All[0], 3), calculate_metrics_regr_popts(filelist_rhorho_Variant_All[0], 5),
                       calculate_metrics_regr_popts(filelist_rhorho_Variant_All[0], 7), calculate_metrics_regr_popts(filelist_rhorho_Variant_All[0], 9),
                       calculate_metrics_regr_popts(filelist_rhorho_Variant_All[0], 11), calculate_metrics_regr_popts(filelist_rhorho_Variant_All[0], 13),
                       calculate_metrics_regr_popts(filelist_rhorho_Variant_All[0], 15), calculate_metrics_regr_popts(filelist_rhorho_Variant_All[0], 17),
                       calculate_metrics_regr_popts(filelist_rhorho_Variant_All[0], 19), calculate_metrics_regr_popts(filelist_rhorho_Variant_All[0], 21)]

           
metrics_Variant_All = np.stack(metrics_Variant_All)


# Now start plotting metrics
# Make better plots here, add axes labels, add color labels, store into figures/*.eps, figures/*.pdf files
# Should we first convert to histograms (?)

#---------------------------------------------------------------------

pathOUT = "figures/"
filename = "rhorho_acc_Variant-All_regr"
x = np.arange(1,11)*2+1
# example plt.plot(x, metrics_Variant_All[:, 0],'o', label=r'$\sigma$' )
plt.plot(x, metrics_Variant_All[:, 0],'o', label='Acc0')
plt.plot(x, metrics_Variant_All[:, 1],'x', label='Acc1')
plt.plot(x, metrics_Variant_All[:, 2],'d', label='Acc2')
plt.plot(x, metrics_Variant_All[:, 3],'v', label='Acc3')
plt.ylim([0.0, 1.3])
plt.xticks(x)
plt.legend()
plt.xlabel('Number of classes')
plt.ylabel('Accuracy')
plt.title('Feautures list: Variant-All')

ax = plt.gca()
plt.tight_layout()

if filename:
    try:
        os.makedirs(pathOUT)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    plt.savefig(pathOUT + filename+".eps")
    print('Saved '+pathOUT + filename+".eps")
    plt.savefig(pathOUT + filename+".pdf")
    print('Saved '+pathOUT + filename+".pdf")
else:
    plt.show()

#---------------------------------------------------------------------
plt.clf()
#---------------------------------------------------------------------

pathOUT = "figures/"
filename = "rhorho_meanDelt_class_Variant-All_regr"

plt.plot(x, metrics_Variant_All[:, 4],'o', label=r'$<\Delta>$ classes')

plt.ylim([0.0, 3.0])
plt.xticks(x)
plt.legend()
plt.xlabel('Number of classes')
plt.ylabel(r'$<\Delta>$ classes')
plt.title('Feautures list: Variant-All')

ax = plt.gca()
plt.tight_layout()

if filename:
    try:
        os.makedirs(pathOUT)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    plt.savefig(pathOUT + filename+".eps")
    print('Saved '+pathOUT + filename+".eps")
    plt.savefig(pathOUT + filename+".pdf")
    print('Saved '+pathOUT + filename+".pdf")
else:
    plt.show()

#---------------------------------------------------------------------
plt.clf()
#---------------------------------------------------------------------

pathOUT = "figures/"
filename = "rhorho_meanDelt_phiCPmix_Variant-All_regr"

plt.plot(x, metrics_Variant_All[:, 7],'o', label=r'$<\Delta \phi^{CP}>$ ')

plt.ylim([0.0, 0.5])
plt.xticks(x)
plt.legend()
plt.xlabel('Number of classes')
plt.ylabel(r'$<\Delta \phi^{CP}>$ (rad)')
plt.title('Feautures list: Variant-All')

ax = plt.gca()
plt.tight_layout()

if filename:
    try:
        os.makedirs(pathOUT)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    plt.savefig(pathOUT + filename+".eps")
    print('Saved '+pathOUT + filename+".eps")
    plt.savefig(pathOUT + filename+".pdf")
    print('Saved '+pathOUT + filename+".pdf")
else:
    plt.show()

#---------------------------------------------------------------------
plt.clf()
#---------------------------------------------------------------------

pathOUT = "figures/"
filename = "rhorho_L1delt_w_Variant_All_regr"

plt.plot(x, metrics_Variant_All[:, 5],'o', label=r'L1 $<\Delta w>$')

plt.ylim([0.0, 0.2])
plt.xticks(x)
plt.legend()
plt.xlabel('Number of classes')
plt.ylabel(r'L1 $<\Delta w>$')
plt.title('Feautures list: Variant-All')

ax = plt.gca()
plt.tight_layout()

if filename:
    try:
        os.makedirs(pathOUT)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    plt.savefig(pathOUT + filename+".eps")
    print('Saved '+pathOUT + filename+".eps")
    plt.savefig(pathOUT + filename+".pdf")
    print('Saved '+pathOUT + filename+".pdf")
else:
    plt.show()
    
#---------------------------------------------------------------------
plt.clf()
#---------------------------------------------------------------------

pathOUT = "figures/"
filename = "rhorho_L2delt_w_Variant_All_regr"

plt.plot(x, metrics_Variant_All[:, 6],'o', label=r'L2 $<\Delta w>$')

plt.ylim([0.0, 0.2])
plt.xticks(x)
plt.legend()
plt.xlabel('Number of classes')
plt.ylabel(r'L2 $<\Delta w>$')
plt.title('Feautures list: Variant-All')

ax = plt.gca()
plt.tight_layout()

if filename:
    try:
        os.makedirs(pathOUT)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    plt.savefig(pathOUT + filename+".eps")
    print('Saved '+pathOUT + filename+".eps")
    plt.savefig(pathOUT + filename+".pdf")
    print('Saved '+pathOUT + filename+".pdf")
else:
    plt.show()
#---------------------------------------------------------------------
plt.clf()
#---------------------------------------------------------------------
 
