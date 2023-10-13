#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/zzyjordan/ryan_do_not_touch/src/kinova-ros/kinova_demo"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/zzyjordan/ryan_do_not_touch/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/zzyjordan/ryan_do_not_touch/install/lib/python2.7/dist-packages:/home/zzyjordan/ryan_do_not_touch/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/zzyjordan/ryan_do_not_touch/build" \
    "/usr/bin/python2" \
    "/home/zzyjordan/ryan_do_not_touch/src/kinova-ros/kinova_demo/setup.py" \
     \
    build --build-base "/home/zzyjordan/ryan_do_not_touch/build/kinova-ros/kinova_demo" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/zzyjordan/ryan_do_not_touch/install" --install-scripts="/home/zzyjordan/ryan_do_not_touch/install/bin"
