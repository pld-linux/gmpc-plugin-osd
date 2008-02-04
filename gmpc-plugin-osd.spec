%define		source_name gmpc-osd
Summary:	A on-screen-display for GMPC
Summary(pl.UTF-8):	Wtyczka OSD dla GMPC
Name:		gmpc-plugin-osd
Version:	0.15.5.0
Release:	1
License:	GPL
Group:		X11/Applications/Sound
# http://download.sarine.nl/gmpc-0.15.5/
Source0:	http://download.sarine.nl/gmpc-0.15.5/%{source_name}-%{version}.tar.gz
# Source0-md5:	2b98c194d83aba2405199b35752117a1
Patch0:		%{name}-plugins_path.patch
URL:		http://gmpc.sarine.nl/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	cairo-devel
BuildRequires:	glib2-devel >= 1:2.10
BuildRequires:	gmpc-devel >= 0.15.5.0
BuildRequires:	gtk+2-devel >= 2:2.8
BuildRequires:	libglade2-devel
BuildRequires:	libmpd-devel >= 0.15.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A on-screen-display for GMPC.

%description -l pl.UTF-8
Wtyczka OSD dla GMPC.

%prep
%setup -qn %{source_name}-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_libdir}/gmpc/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gmpc/*.so
