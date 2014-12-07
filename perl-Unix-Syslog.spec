%define	module	Unix-Syslog
%define upstream_version 1.1

Summary:	Perl interface to the UNIX system logger
Name:		perl-%{module}
Version:	%perl_convert_version %{upstream_version}
Release:	19
License:	GPLv2
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}/
Source0:	http://www.cpan.org/modules/by-module/Unix/%{module}-%{upstream_version}.tar.gz
Buildrequires:	perl-devel

%description
This module provides access to the system logger available on most
UNIX systems via perl XSUBs (perl's C interface).

%prep
%setup -qn %{module}-%{upstream_version}

%build
CFLAGS="%{optflags}" %__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%{perl_vendorarch}/*
%{_mandir}/man3/*

