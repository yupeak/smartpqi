Name:           smartpqi
Version:        0.0.1 
Release:        1%{?dist}
Summary:        Install Smartpqi kernel driver   

License:       GPL 
URL:           na 
Source0:       %{name}-%{version}.tar.gz 

BuildRequires: bash 
Requires:      bash 

%description
Install Smartpqi kernal driver

%prep
%setup -q


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/etc/depmod.d
mkdir -p %{buildroot}/etc/dracut.conf.d
mkdir -p %{buildroot}/lib/modules/$(uname -r)/extra/smartpqi
cp -a lib/modules/3.14.4-200.fc20.x86_64/extra/smartpqi/smartpqi.ko %{buildroot}/lib/modules/3.14.4-200.fc20.x86_64/extra/smartpqi
cp -a etc/depmod.d/smartpqi.conf %{buildroot}/etc/depmod.d
cp -a etc/dracut.conf.d/smartpqi.conf %{buildroot}/etc/dracut.conf.d

%files
/etc/depmod.d/smartpqi.conf
/etc/dracut.conf.d/smartpqi.conf
/lib/modules/3.14.4-200.fc20.x86_64/extra/smartpqi/smartpqi.ko

%post
/usr/sbin/depmod -a
/usr/sbin/modprobe -v smartpqi



%changelog
* Sat Jun  1 2024 root
- 
