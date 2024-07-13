# This file is part of Xpra.
# Copyright (C) 2011-2018 Antoine Martin <antoine@xpra.org>
# Xpra is released under the terms of the GNU GPL v2, or, at your option, any
# later version. See the file COPYING for details.

from xpra.util import envbool
from xpra.notifications.notifier_base import NotifierBase, log
from xpra.platform.win32.win32_balloon import notify
from xpra.gtk_common import gtk_notifier

try:
    from xpra.gtk_common.gtk_notifier import GTK_Notifier
    GTK_NOTIFIER = envbool("XPRA_WIN32_GTK_NOTIFIER", False)
except ImportError:
    GTK_Notifier = None
    GTK_NOTIFIER = False


class Win32_Notifier(NotifierBase):

    def __init__(self, *args):
        NotifierBase.__init__(self, *args)
        self.handles_actions = GTK_Notifier is not None
        self.gtk_notifier = None
        self.gtk_notifications = set()
        self.notification_handles = {}

    def get_gtk_notifier(self):
        if self.gtk_notifier is None:
            try:
                self.gtk_notifier = GTK_Notifier(self.closed_cb, self.action_cb)
            except:
                log("failed to load GTK Notifier fallback", exc_info=True)
        return self.gtk_notifier

    def show_notify(self, dbus_id, tray, nid, app_name, replaces_nid, app_icon, summary, body, actions, hints, expire_timeout, icon):
        if not tray:
            log("cannot show notifications without a tray")
            return
        getHWND = getattr(tray, "getHWND", None)
        if GTK_NOTIFIER and (actions or not getHWND):
            gtk_notifier = self.get_gtk_notifier()
            if gtk_notifier:
                gtk_notifier.show_notify(dbus_id, tray, nid, app_name, replaces_nid, app_icon, summary, body, actions, hints, expire_timeout, icon)
                self.gtk_notifications.add(nid)
                return
        if not getHWND:
            log.warn("Warning: missing 'getHWND' on %s (%s)", tray, type(tray))
            return
        if tray is None:
            log.warn("Warning: no system tray - cannot show notification!")
            return
        hwnd = getHWND()
        app_id = tray.app_id
        log("show_notify%s hwnd=%#x, app_id=%i", (dbus_id, tray, nid, app_name, replaces_nid, app_icon, summary, body, actions, hints, expire_timeout, icon), hwnd, app_id)
        #FIXME: remove handles when notification is closed
        self.notification_handles[nid] = (hwnd, app_id)
        notify(hwnd, app_id, summary, body, expire_timeout, icon)

    def close_notify(self, nid):
        try:
            self.gtk_notifications.remove(nid)
            if self.gtk_notifier:
                self.gtk_notifier.close_notify(nid)
        except KeyError:
            try:
                hwnd, app_id = self.notification_handles.pop(nid)
            except KeyError:
                return
            log("close_notify(%i) hwnd=%i, app_id=%i", nid, hwnd, app_id)
            notify(hwnd, app_id, "", "", 0, None)
        else:
            self.get_gtk_notifier().close_notify(nid)
