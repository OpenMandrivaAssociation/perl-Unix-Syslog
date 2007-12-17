%define	module	Unix-Syslog
%define	name	perl-%{module}
%define	version	1.0
%define	release	%mkrel 1

Name:		%{name}
Summary:	Perl interface to the UNIX system logger
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Perl
URL:		http://www.cpan.org/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{module}/%{module}-%{version}.tar.bz2
Buildrequires:	perl-devel

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
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std}

%clean
rm -rf $RPM_BUILD_ROOT 

%files
%defattr(-,root,root)
%{perl_vendorarch}/*
%{_mandir}/*/*

