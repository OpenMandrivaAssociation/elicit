%define	name	elicit
%define	version	0.9.3
%define svn 20090227
%define release %mkrel 0.%{svn}.2


Summary: 	Enlightenment screen zoom
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	BSD
Group: 		Graphical desktop/Enlightenment
URL: 		http://get-e.org/
Source: 	%{name}-%{version}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires:	evas-devel >= 0.9.9.050, esmart-devel >= 0.9.0.050, embryo-devel >= 0.9.9.050
BuildRequires:	ecore-devel >= 0.9.9.050, edje-devel >= 0.9.9.050
BuildRequires:	eet-devel >= 1.1.0, eet >= 1.1.0
BuildRequires:	edje >= 0.9.9.050
#Buildrequires:	edb-devel

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
