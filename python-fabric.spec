Name:		python-fabric
Version:	2.7.1
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/f/fabric/fabric-%{version}.tar.gz
Summary:	High level SSH command execution
URL:		https://pypi.org/project/fabric/
License:	BSD
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
High level SSH command execution

%prep
%autosetup -p1 -n fabric-%{version}

%build
%py_build

%install
%py_install

%files
%{_bindir}/fab
%{py_sitedir}/fabric
%{py_sitedir}/fabric-*.*-info
