%define	module	Unix-Syslog
%define	name	perl-%{module}
%define	version	1.1
%define	release	%mkrel 8

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



%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.1-8mdv2012.0
+ Revision: 765800
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.1-7
+ Revision: 764323
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1-6
+ Revision: 667410
- mass rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 1.1-5mdv2011.0
+ Revision: 564592
- rebuild for perl 5.12.1

* Tue Jul 20 2010 J√©r√¥me Quelin <jquelin@mandriva.org> 1.1-4mdv2011.0
+ Revision: 555210
- rebuild

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.1-3mdv2010.1
+ Revision: 426600
- rebuild

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.1-2mdv2009.0
+ Revision: 265450
- rebuild early 2009.0 package (before pixel changes)

* Wed May 21 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.1-1mdv2009.0
+ Revision: 209846
- new version

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 1.0-2mdv2008.1
+ Revision: 151401
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Oct 21 2007 Funda Wang <fwang@mandriva.org> 1.0-1mdv2008.1
+ Revision: 100849
- New version 1.0

* Sat May 05 2007 Olivier Thauvin <nanardon@mandriva.org> 0.100-4mdv2008.0
+ Revision: 23249
- rebuild


* Mon May 01 2006 Stefan van der Eijk <stefan@eijk.nu> 0.100-3mdk
-_rebuild_for_sparc

* Tue Nov 16 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.100-2mdk
- rebuild for new perl

* Thu Jun 03 2004 Per ÿyvind Karlsen <peroyvind@linux-mandrake.com> 0.100-1mdk
- 0.100
- cosmetics

* Thu Aug 14 2003 Per ÿyvind Karlsen <peroyvind@linux-mandrake.com> 0.99-4mdk
- rebuild for new perl
- don't rm -rf $RPM_BUILD_ROOT in %%prep
- use %%makeinstall_std macro

* Tue May 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.99-3mdk
- rebuild for new auto{prov,req}

* Mon May 05 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.99-2mdk
- buildrequires

