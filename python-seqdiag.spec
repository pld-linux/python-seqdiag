# TODO
# - unpackaged files
#   /usr/share/python2.7/site-packages/seqdiag_sphinxhelper.pyc
#   /usr/share/python2.7/site-packages/seqdiag_sphinxhelper.pyo
#   /usr/share/python2.7/site-packages/sphinxcontrib_seqdiag.pyc
#   /usr/share/python2.7/site-packages/sphinxcontrib_seqdiag.pyo
%define 	module	seqdiag
Summary:	seqkdiag generate sequence-diagram image file from spec-text file
Name:		python-%{module}
Version:	0.4.2
Release:	0.2
License:	Apache v2.0
Group:		Development/Languages
URL:		http://blockdiag.com/en/seqdiag/index.html
Source0:	http://pypi.python.org/packages/source/s/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	d13415c44193ca6e3c6409dbb73cd693
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	sed >= 4.0
Requires:	python-blockdiag
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
seqdiag generates sequence-diagram image file from spec-text files.

Features:
- Generate sequence-diagram from dot like text (basic feature).
- Multilingualization for node-label (utf-8 only).

%prep
%setup -q -n %{module}-%{version}
%{__sed} -i -e 's/^from ez_setup/#from ez_setup/' setup.py
%{__sed} -i -e 's/^use_setuptools()/#use_setuptools()/' setup.py

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--skip-build \
	--root $RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}/tests
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/seqdiag
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-%{version}-*.egg-info
%endif
