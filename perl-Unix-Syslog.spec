%define	module	Unix-Syslog
%define	name	perl-%{module}
%define	version	1.1
%define	release	%mkrel 3

Name:		%{name}
Summary:	Perl interface to the UNIX system logger
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}/
Source:     http://www.cpan.org/modules/by-module/Unix/%{module}-%{version}.tar.gz
Buildrequires:	perl-devel
Buildroot:	%{_tmppath}/%{name}-%{version}

%description
This module provides access to the system logger available on most
UNIX systems via perl XSUBs (perl's C interface).

%prep
%setup -q -n %{module}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" %{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%{makeinstall_std}

%clean
rm -rf %{buildroot} 

%files
%defattr(-,root,root)
%{perl_vendorarch}/*
%{_mandir}/*/*

