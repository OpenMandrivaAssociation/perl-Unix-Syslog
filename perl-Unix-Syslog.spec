%define	module	Unix-Syslog

Summary:	Perl interface to the UNIX system logger
Name:		perl-%{module}
Version:	1.1
Release:	10
License:	GPLv2
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}/
Source0:	http://www.cpan.org/modules/by-module/Unix/%{module}-%{version}.tar.gz
Buildrequires:	perl-devel

%description
This module provides access to the system logger available on most
UNIX systems via perl XSUBs (perl's C interface).

%prep
%setup -qn %{module}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" %__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%{perl_vendorarch}/*
%{_mandir}/man3/*

