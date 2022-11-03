#! /usr/bin/env python3
from pylab import *

figure(1, figsize = (8, 8))
ax = axes()

# old vla
data = genfromtxt('saturn.tab', comments = '!')
wave = data[:,0]
tb = data[:,1]
tb_err = data[:,2]

ax.errorbar(wave, tb, yerr = tb_err, label = 'Old VLA',
  color = 'C0', fmt = 'o', mfc = 'none', capsize = 5)

# zz data
data = genfromtxt('saturn.tabZZ.dat')
freq = data[:,0]  # GHz
tb =  data[:,5]
tb_err = data[:,6]

ax.errorbar(30./freq, tb, yerr = tb_err, label = '?ZZ?',
  color = 'C1', fmt = 'o', mfc = 'none', capsize = 5)

# old saturn
data = genfromtxt('saturn.tbv', comments = '!')
wave = data[:,0] # cm
tb = data[:,2]
tb_err = data[:,3]

ax.errorbar(wave, tb, yerr = tb_err, label = '?TBV?',
  color = 'C2', fmt = 'o', mfc = 'none', capsize = 5)

# planck data
data = genfromtxt('planck_saturn.dat')
freq = data[:,0] # GHz
tb = data[:,2]
tb_err = data[:,3]

ax.errorbar(30./freq, tb, yerr = tb_err, label = 'Planck',
  color = 'C4', fmt = 'o', capsize = 5)

# bima03
data = genfromtxt('saturn.bima03')
wave = data[:,0] # cm
tb = data[:,1]
tb_err = data[:,2]

ax.errorbar(wave, tb, yerr = tb_err, label = 'BIMA03',
  color = 'C4', fmt = 'o', capsize = 5)

# wmap
data = genfromtxt('wmap_saturn.dat')
freq = data[:,0] # GHz
tb = data[:,5]
tb_err = data[:,6]

ax.errorbar(30./freq, tb, yerr = tb_err, label = 'WMAP',
  color = 'C5', fmt = 'o', capsize = 5)

# GMRT
data = genfromtxt('saturn_GMRT.tab')
wave = data[:,0]  # cm
tb = data[:,1]
tb_err = data[:,2]

ax.errorbar(wave, tb, yerr = tb_err, label = 'GMRT',
  color = 'C6', fmt = 'o', capsize = 5)

ax.set_xscale('log')
ax.set_xticks([0.01, 0.05, 0.1, 0.5, 1., 5, 10., 50., 100.])
ax.set_xlabel('Wavelength (cm)', fontsize = 12)
ax.set_ylabel('Brightness temperature (K)', fontsize = 12)
ax.legend(fontsize = 12)
ax.set_ylim([100., 620.])
ax.set_xlim([1.E-2, 150.])

savefig('saturn_radio_data.png', bbox_inches = 'tight')
