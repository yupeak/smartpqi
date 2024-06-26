How to compile Smartpqi kernel driver from source and build rpm package

# Clone git source tree 

  -  mkdir -p ~/Projects
  -  cd ~/Projects
  -  git clone https://github.com/yupeak/smartpqi.git
  -  cd smartpqi
  -  make -f Makefile.alt


# 3) Build rpm package

-  rpmdev-setuptree 
-  cd ~/rpmbuuild
-  cd BUILDROOT
-  mkdir -p smartpqi-0.0.1
-  cd smartpqi-0.0.1
-  mkdir -p etc/depmod.d/
-  mkdir -p etc/dracut.conf.d
-  mkdir -p lib/modules/3.14.4-200.fc20.x86_64/extra/

-  cp ~/Projects/smartpqi/depmod.d/smartpqi.conf etc/depmod.d/
-  cp ~/Projects/smartpqi/dracut.conf.d/smartpqi.conf etc/dracut.conf.d/
-  cp smartpqi.ko lib/modules/3.14.4-200.fc20.x86_64/extra/smartpqi/

-  tar -cvzf smartpqi-0.0.1.tgz smartpqi-0.0.1
-  mv smartpqi-0.0.1.tgz ../SOURCES

-  rpmdev-newspec smartpqi

# Build binary and source rpm packages.

use rpmbuild -ba ~/rpmbuild/SPECS/smartpqi.spec
- cp smartpqi.spec ~/rpmbuild/SPECS

# rpm build options: 
-  bb for binary rpm only
-  bs for source rpm only

# Option 1:Use prebuild rpm package for Fedora 20 3.14.4-200.fc20.x86_64.

-  Use the rpm in rpmbuild/RPMS/x86_64/smartpqi-0.0.1-1.fc20.x86_64.rpm

# Option 2: Manually copy files and load smartpqi driver. 

-  mkdir -p /lib/modules/3.14.4-200.fc20.x86_64/extra/smartpqi/
-  cp smartpqi.ko /lib/modules/3.14.4-200.fc20.x86_64/extra/smartpqi/

# Copy config file so module can be loaded upon reboot

-  cp depmod.d/smartpqi.conf /etc/depmod.d/
-  cp dracut.conf.d/smartpqi.conf /etc/dracut.conf.d/

# Manually Load kernel module

-  depmod -a
-  modprobe smartpqi
