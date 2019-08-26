import numpy as np
from glob import glob
import os, errno

import matplotlib.pyplot as plt

from anal_utils import calculate_metrics_from_file

filelist_rhorho_Variant_1_1 = []

filelist_rhorho_Variant_1_1.append('../laptop_results/nn_rhorho_Variant-All_soft_Unweighted_False_NO_NUM_CLASSES_2/monit_npy/')
filelist_rhorho_Variant_1_1.append('../laptop_results/nn_rhorho_Variant-All_soft_Unweighted_False_NO_NUM_CLASSES_4/monit_npy/')
filelist_rhorho_Variant_1_1.append('../laptop_results/nn_rhorho_Variant-All_soft_Unweighted_False_NO_NUM_CLASSES_6/monit_npy/')
filelist_rhorho_Variant_1_1.append('../laptop_results/nn_rhorho_Variant-All_soft_Unweighted_False_NO_NUM_CLASSES_8/monit_npy/')
filelist_rhorho_Variant_1_1.append('../laptop_results/nn_rhorho_Variant-All_soft_Unweighted_False_NO_NUM_CLASSES_10/monit_npy/')
filelist_rhorho_Variant_1_1.append('../laptop_results/nn_rhorho_Variant-All_soft_Unweighted_False_NO_NUM_CLASSES_12/monit_npy/')
filelist_rhorho_Variant_1_1.append('../laptop_results/nn_rhorho_Variant-All_soft_Unweighted_False_NO_NUM_CLASSES_14/monit_npy/')
filelist_rhorho_Variant_1_1.append('../laptop_results/nn_rhorho_Variant-All_soft_Unweighted_False_NO_NUM_CLASSES_16/monit_npy/')
filelist_rhorho_Variant_1_1.append('../laptop_results/nn_rhorho_Variant-All_soft_Unweighted_False_NO_NUM_CLASSES_18/monit_npy/')
filelist_rhorho_Variant_1_1.append('../laptop_results/nn_rhorho_Variant-All_soft_Unweighted_False_NO_NUM_CLASSES_20/monit_npy/')


metrics_Variant_1_1 = [calculate_metrics_from_file(filelist_rhorho_Variant_1_1[0], 2), calculate_metrics_from_file(filelist_rhorho_Variant_1_1[1], 4),
                       calculate_metrics_from_file(filelist_rhorho_Variant_1_1[2], 6), calculate_metrics_from_file(filelist_rhorho_Variant_1_1[3], 8),
                       calculate_metrics_from_file(filelist_rhorho_Variant_1_1[4], 10), calculate_metrics_from_file(filelist_rhorho_Variant_1_1[5], 12),
                       calculate_metrics_from_file(filelist_rhorho_Variant_1_1[6], 14), calculate_metrics_from_file(filelist_rhorho_Variant_1_1[7], 16),
                       calculate_metrics_from_file(filelist_rhorho_Variant_1_1[8], 18), calculate_metrics_from_file(filelist_rhorho_Variant_1_1[9], 20)]
           
metrics_Variant_1_1 = np.stack(metrics_Variant_1_1)


# Now start plotting metrics
# Make better plots here, add axes labels, add color labels, store into figures/*.eps, figures/*.pdf files
# Should we first convert to histograms (?)

#---------------------------------------------------------------------

pathOUT = "figures/"
filename = "rhorho_acc_Variant-All_nc"
x = np.arange(1,11)*2
# example plt.plot(x, metrics_Variant_1_1[:, 0],'o', label=r'$\sigma$' )
plt.plot(x, metrics_Variant_1_1[:, 0],'o', label=r'$|\Delta_{class}| < 1$')
plt.plot(x, metrics_Variant_1_1[:, 1],'x', label=r'$|\Delta_{class}| < 2$')
plt.plot(x, metrics_Variant_1_1[:, 2],'d', label=r'$|\Delta_{class}| < 3$')
plt.plot(x, metrics_Variant_1_1[:, 3],'v', label=r'$|\Delta_{class}| < 4$')
plt.ylim([0.0, 1.5])
plt.xticks(x)
plt.legend()
plt.xlabel(r'$N_{class}$')
plt.ylabel('Fraction')
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
filename = "rhorho_meanDelt_class_Variant-All_nc"

plt.plot(x, metrics_Variant_1_1[:, 4],'o', label=r'$<\Delta>_{class}$')

plt.ylim([-1.0, 1.0])
plt.xticks(x)
plt.legend()
plt.xlabel(r'$N_{class}$')
plt.ylabel(r'$<\Delta>_{class}$')
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
filename = "rhorho_meanDelt_phiCPmix_Variant-All_nc"

plt.plot(x, metrics_Variant_1_1[:, 7],'o', label=r'$<\Delta \alpha^{CP}> [rad]$ ')

#plt.ylim([0.0, 0.5])
plt.xticks(x)
plt.legend()
plt.ylim([-0.5, 0.5])
plt.xlabel(r'$N_{class}$')
plt.ylabel(r'$<\Delta \alpha^{CP}>$ [rad]')
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
filename = "rhorho_L1delt_w_Variant_All_nc"

plt.plot(x, metrics_Variant_1_1[:, 5],'o', label=r'$l_1$')

plt.ylim([0.0, 0.1])
plt.xticks(x)
plt.legend()
plt.xlabel(r'$N_{class}$')
plt.ylabel(r'$l_1$')
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
filename = "rhorho_L2delt_w_Variant_All_nc"

plt.plot(x, metrics_Variant_1_1[:, 6],'o', label=r'$l_2$')

plt.ylim([0.0, 0.1])
plt.xticks(x)
plt.legend()
plt.xlabel(r'$N_{class}$')
plt.ylabel(r'$l_2$')
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
 
