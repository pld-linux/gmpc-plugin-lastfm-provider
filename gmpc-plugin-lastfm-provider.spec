%define		source_name gmpc-lastfm
Summary:	Last.fm provider plugin for Gnome Music Player Client
Summary(pl.UTF-8):	Wtyczka udostępniająca dane z Last.fm dla odtwarzacza Gnome Music Player Client
Name:		gmpc-plugin-lastfm-provider
Version:	0.14.0
Release:	1
License:	GPL
Group:		X11/Applications/Sound
# http://sarine.nl/gmpc-plugins-downloads
Source0:	%{source_name}-%{version}.tar.gz
# Source0-md5:	1ace7659c98b0a20e5962ab2da83c0a5
Patch0:		%{name}-plugins_path.patch
URL:		http://sarine.nl/gmpc-plugins-lastfm
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gmpc-devel >= 0.14.0
BuildRequires:	gtk+2-devel >= 2:2.4
BuildRequires:	libglade2-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The last.fm plugin can fetch artist images, from last.fm. This plugin doesn't
scrobble your music, use a dedicated client like mpdscribble for this.

%description -l pl.UTF-8
Ta wtyczka pobiera obrazy oraz informacje o artyście z Last.fm. Nie wysyła ona
informacji o odtwarzanych utworach. W tym celu należy skorzystać z dedykowanego
klienta jak mpdscribble.

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
install -d $RPM_BUILD_ROOT%{_libdir}/gmpc

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_libdir}/gmpc/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gmpc/*.so
