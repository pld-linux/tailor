Summary:	A tool to migrate changesets between several version control systems
Name:		tailor
Version:	0.9.35
Release:	1
Source0:	http://darcs.arstecnica.it/tailor/%{name}-%{version}.tar.gz
# Source0-md5:	58a6bc1c1d922b0b1e4579c6440448d1
License:	GPL v3+
Group:		Development/Tools
URL:		http://progetti.arstecnica.it/tailor
Patch0:		%{name}-test.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=477148
# http://progetti.arstecnica.it/tailor/ticket/172
Patch1:		mercurial-1.1-compat.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=478841
Patch2:		mercurial-1.1.2-delete.patch
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-vcpx = %{version}-%{release}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tailor is a tool to migrate changesets between Aegis, ArX, Bazaar,
Bazaar-NG, CVS, Codeville, Darcs, Git, Mercurial, Monotone, Perforce,
Subversion and Tla repositories.

This script makes it easier to keep the upstream changes merged in a
branch of a product, storing needed information such as the upstream
URI and revision in special properties on the branched directory.

%package -n python-vcpx
Summary:	Version Control Patch eXchanger
Group:		Development/Libraries
Requires:	cvs
Requires:	git-core
Requires:	mercurial >= 1.1.2
Requires:	monotone
Requires:	subversion

%description -n python-vcpx
This is the package `vcpx` (pronounced "veeseepex"). It encapsulates
the machinery needed to keep the patches in sync across different VC
systems.

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p1

# remove the shebang line
%{__sed} -i -e '1d' vcpx/repository/p4/p4lib.py

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.html
%attr(755,root,root) %{_bindir}/%{name}

%files -n python-vcpx
%defattr(644,root,root,755)
%{py_sitescriptdir}/tailor-%{version}-*.egg-info
%dir %{py_sitescriptdir}/vcpx
%{py_sitescriptdir}/vcpx/*.py[co]
%dir %{py_sitescriptdir}/vcpx/repository
%{py_sitescriptdir}/vcpx/repository/*.py[co]
%dir %{py_sitescriptdir}/vcpx/repository/aegis
%{py_sitescriptdir}/vcpx/repository/aegis/*.py[co]
%dir %{py_sitescriptdir}/vcpx/repository/darcs
%{py_sitescriptdir}/vcpx/repository/darcs/*.py[co]
%dir %{py_sitescriptdir}/vcpx/repository/git
%{py_sitescriptdir}/vcpx/repository/git/*.py[co]
%dir %{py_sitescriptdir}/vcpx/repository/p4
%{py_sitescriptdir}/vcpx/repository/p4/*.py[co]
