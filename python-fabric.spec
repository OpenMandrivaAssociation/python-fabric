%define module fabric

Name:		python-fabric
Version:	3.2.3
Release:	1
Summary:	High level SSH command execution
License:	BSD
Group:		Development/Python
URL:		https://pypi.org/project/fabric/
Source0:	https://files.pythonhosted.org/packages/source/f/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
High level SSH command execution

%prep -a
# Remove bundled egg-info
rm -rf %{module}.egg-info

%files
%{_bindir}/fab
%{py_sitedir}/%{module}
%{py_sitedir}/%{module}-%{version}*.*-info
