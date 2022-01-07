#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-iniconfig
Version  : 1.1.1
Release  : 19
URL      : https://files.pythonhosted.org/packages/23/a2/97899f6bd0e873fed3a7e67ae8d3a08b21799430fb4da15cfedf10d6e2c2/iniconfig-1.1.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/23/a2/97899f6bd0e873fed3a7e67ae8d3a08b21799430fb4da15cfedf10d6e2c2/iniconfig-1.1.1.tar.gz
Summary  : iniconfig: brain-dead simple config-ini parsing
Group    : Development/Tools
License  : MIT
Requires: pypi-iniconfig-license = %{version}-%{release}
Requires: pypi-iniconfig-python = %{version}-%{release}
Requires: pypi-iniconfig-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
Provides: iniconfig
Provides: iniconfig-python
Provides: iniconfig-python3
BuildRequires : pypi(pluggy)
BuildRequires : py-python
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(wheel)
BuildRequires : pytest
BuildRequires : setuptools_scm
BuildRequires : tox
BuildRequires : pypi(virtualenv)

%description
=======================================================
        
        iniconfig is a small and simple INI-file parser module

%package license
Summary: license components for the pypi-iniconfig package.
Group: Default

%description license
license components for the pypi-iniconfig package.


%package python
Summary: python components for the pypi-iniconfig package.
Group: Default
Requires: pypi-iniconfig-python3 = %{version}-%{release}

%description python
python components for the pypi-iniconfig package.


%package python3
Summary: python3 components for the pypi-iniconfig package.
Group: Default
Requires: python3-core
Provides: pypi(iniconfig)

%description python3
python3 components for the pypi-iniconfig package.


%prep
%setup -q -n iniconfig-1.1.1
cd %{_builddir}/iniconfig-1.1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641445283
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-iniconfig
cp %{_builddir}/iniconfig-1.1.1/LICENSE %{buildroot}/usr/share/package-licenses/pypi-iniconfig/cf3eaf29116a37a7d9ba773e776104c067c8e5fc
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-iniconfig/cf3eaf29116a37a7d9ba773e776104c067c8e5fc

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
