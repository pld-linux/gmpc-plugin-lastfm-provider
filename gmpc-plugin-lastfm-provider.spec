%define		source_name gmpc-last-fm
Summary:	Last.fm provider plugin for Gnome Music Player Client
Summary(pl.UTF-8):	Wtyczka udostępniająca dane z Last.fm dla odtwarzacza Gnome Music Player Client
Name:		gmpc-plugin-lastfm-provider
Version:	0.20.0
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://downloads.sourceforge.net/musicpd/%{source_name}-%{version}.tar.gz
# Source0-md5:	aa5ae094e1bb78a11de9dd6e12f0bfb7
URL:		http://gmpc.wikia.com/wiki/GMPC_PLUGIN_LASTFM
BuildRequires:	autoconf >= 2.58
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 2.16
BuildRequires:	gmpc-devel >= 0.19.0
BuildRequires:	gtk+2-devel >= 2:2.4
BuildRequires:	intltool >= 0.21
BuildRequires:	libglade2-devel
BuildRequires:	libmpd-devel >= 0.15.98
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig
Requires:	gmpc >= 0.19.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The last.fm plugin can fetch artist images, from last.fm. This plugin
doesn't scrobble your music, use a dedicated client like mpdscribble
for this.

%description -l pl.UTF-8
Ta wtyczka pobiera obrazy oraz informacje o artyście z Last.fm. Nie
wysyła ona informacji o odtwarzanych utworach. W tym celu należy
skorzystać z dedykowanego klienta jak mpdscribble.

%prep
%setup -qn %{source_name}-%{version}

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
install -d $RPM_BUILD_ROOT%{_libdir}/gmpc

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name

rm $RPM_BUILD_ROOT%{_libdir}/gmpc/plugins/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gmpc/plugins/*.so
