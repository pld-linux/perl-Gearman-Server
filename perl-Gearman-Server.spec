#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define	pdir	Gearman
%define	pnam	Server
%include	/usr/lib/rpm/macros.perl
Summary:	Gearman::Server - function call "router" and load balancer
Name:		perl-Gearman-Server
Version:	1.09
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/B/BR/BRADFITZ/Gearman-Server-%{version}.tar.gz
# Source0-md5:	3d107089f7266ab91d66d9a7bd90430f
URL:		http://search.cpan.org/dist/Gearman-Server/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
You run a Gearman server (or more likely, many of them for both
high-availability and load balancing), then have workers (using
Gearman::Worker from the Gearman module, or libraries for other
languages) register their ability to do certain functions to all of
them, and then clients (using Gearman::Client, Gearman::Client::Async,
etc) request work to be done from one of the Gearman servers.

The servers connect them, routing function call requests to the
appropriate workers, multiplexing responses to duplicate requests as
requested, etc.

More than likely, you want to use the provided gearmand wrapper
script, and not use Gearman::Server directly.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES
%{perl_vendorlib}/Gearman/*.pm
%{perl_vendorlib}/Gearman/Server
%{_mandir}/man3/*
%attr(755,root,root) %{_bindir}/gearmand
%{_mandir}/man1/*
