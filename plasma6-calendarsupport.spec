#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define major 6
%define libname %mklibname KF6CalendarSupport
%define devname %mklibname KF6CalendarSupport -d

Name: plasma6-calendarsupport
Version:	24.12.3
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release:	%{?git:0.%{git}.}2
%if 0%{?git:1}
Source0:	https://invent.kde.org/pim/calendarsupport/-/archive/%{gitbranch}/calendarsupport-%{gitbranchd}.tar.bz2#/calendarsupport-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{ftpdir}/release-service/%{version}/src/calendarsupport-%{version}.tar.xz
%endif
Summary: KDE library for calendar handling
URL: https://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6PrintSupport)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6UiTools)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6GuiAddons)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KPim6Mime)
BuildRequires: cmake(KPim6AkonadiMime)
BuildRequires: cmake(KF6Codecs)
BuildRequires: cmake(KPim6CalendarUtils)
BuildRequires: cmake(KF6CalendarCore)
BuildRequires: cmake(KPim6IdentityManagementCore)
BuildRequires: cmake(KF6Holidays)
BuildRequires: cmake(KPim6AkonadiCalendar)
BuildRequires: cmake(KPim6PimCommon)
BuildRequires: cmake(KPim6IMAP)
BuildRequires: cmake(KPim6Libkdepim)
BuildRequires: cmake(KPim6Akonadi)
BuildRequires: cmake(KPim6AkonadiNotes)
BuildRequires: boost-devel
BuildRequires: sasl-devel
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt6-qttools-assistant

%description
KDE library for calendar handling.

%package -n %{libname}
Summary: KDE library for calendar handling
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
KDE library for calendar handling.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%autosetup -p1 -n calendarsupport-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang calendarsupport6

%files -f calendarsupport6.lang
%{_datadir}/qlogging-categories6/calendarsupport.categories
%{_datadir}/qlogging-categories6/calendarsupport.renamecategories

%files -n %{libname}
%{_libdir}/*.so.*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
