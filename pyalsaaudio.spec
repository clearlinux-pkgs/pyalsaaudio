#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyalsaaudio
Version  : 0.8.4
Release  : 2
URL      : https://files.pythonhosted.org/packages/52/b6/44871791929d9d7e11325af0b7be711388dfeeab17147988f044a41a6d83/pyalsaaudio-0.8.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/52/b6/44871791929d9d7e11325af0b7be711388dfeeab17147988f044a41a6d83/pyalsaaudio-0.8.4.tar.gz
Summary  : ALSA bindings
Group    : Development/Tools
License  : Python-2.0
Requires: pyalsaaudio-license = %{version}-%{release}
Requires: pyalsaaudio-python = %{version}-%{release}
Requires: pyalsaaudio-python3 = %{version}-%{release}
BuildRequires : alsa-lib-dev
BuildRequires : buildreq-distutils3

%description
It is fairly complete for PCM devices and Mixer access.

%package license
Summary: license components for the pyalsaaudio package.
Group: Default

%description license
license components for the pyalsaaudio package.


%package python
Summary: python components for the pyalsaaudio package.
Group: Default
Requires: pyalsaaudio-python3 = %{version}-%{release}

%description python
python components for the pyalsaaudio package.


%package python3
Summary: python3 components for the pyalsaaudio package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pyalsaaudio package.


%prep
%setup -q -n pyalsaaudio-0.8.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1541255197
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pyalsaaudio
cp LICENSE %{buildroot}/usr/share/package-licenses/pyalsaaudio/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pyalsaaudio/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
