%define	name	elicit
%define	version	0.9.0
%define release 0.%{cvsrel}.1mdk

%define cvsrel 20060323

Summary: 	Enlightenment screen zoom
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	BSD
Group: 		Graphical desktop/Enlightenment
URL: 		http://get-e.org/
Source: 	%{name}-%{cvsrel}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires:	evas-devel esmart-devel embryo-devel
BuildRequires:	ecore-devel edje-devel 
BuildRequires:	edb-devel eet-devel
BuildRequires:	edje

%description
Elicit is a screen zoomer / color picker written with the Enlightenment
Foundation Libraries

This package is part of the Enlightenment DR17 desktop shell.

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q -n %name

%build
./autogen.sh
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README
%{_bindir}/*
%{_datadir}/%name
