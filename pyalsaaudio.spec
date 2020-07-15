#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyalsaaudio
Version  : 0.9.0
Release  : 10
URL      : https://files.pythonhosted.org/packages/23/b1/672d496718562301ce2052b07196ca31874e4f1a497881ae44b2279a4e1d/pyalsaaudio-0.9.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/23/b1/672d496718562301ce2052b07196ca31874e4f1a497881ae44b2279a4e1d/pyalsaaudio-0.9.0.tar.gz
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
Provides: pypi(pyalsaaudio)

%description python3
python3 components for the pyalsaaudio package.


%prep
%setup -q -n pyalsaaudio-0.9.0
cd %{_builddir}/pyalsaaudio-0.9.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1594825406
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pyalsaaudio
cp %{_builddir}/pyalsaaudio-0.9.0/LICENSE %{buildroot}/usr/share/package-licenses/pyalsaaudio/bf948988e1d6850c18ac24c94ce9604f4d3fc890
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pyalsaaudio/bf948988e1d6850c18ac24c94ce9604f4d3fc890

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
