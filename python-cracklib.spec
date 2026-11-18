Summary:	Python 2 binding for cracklib
Summary(pl.UTF-8):	Wiązanie Pythona 2 do crackliba
Name:		python-cracklib
# keep 2.10.3 here, it's the last version with python2 support
Version:	2.10.3
Release:	1
License:	LGPL v2.1+
Group:		Libraries
#Source0Download: https://github.com/cracklib/cracklib/releases
Source0:	https://github.com/cracklib/cracklib/releases/download/v%{version}/cracklib-%{version}.tar.xz
# Source0-md5:	e8ea2b86de774fc09fdd0f2829680b19
Patch0:		python-flags.patch
Patch1:		cracklib-system-lib.patch
URL:		https://github.com/cracklib/cracklib
BuildRequires:	cracklib-devel >= %{version}
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	cracklib%{?_isa} >= %{version}
Requires:	python-libs%{?_isa} >= 1:2.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python 2 binding for cracklib.

%description -l pl.UTF-8
Wiązanie Pythona 2 do crackliba.

%prep
%setup -q -n cracklib-%{version}
%patch -P0 -p1
%patch -P1 -p1

%{__sed} -e 's/@VERSION@/%{version}/' python/setup.py.in >python/setup.py

%build
cd python
%py_build

%install
rm -rf $RPM_BUILD_ROOT

cd python
%py_install

%py_postclean
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/test_cracklib.py*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitedir}/_cracklib.so
%{py_sitedir}/cracklib.py[co]
%{py_sitedir}/cracklib-%{version}-py*.egg-info
