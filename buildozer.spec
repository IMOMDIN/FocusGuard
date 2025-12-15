[app]

title = FocusGuard
package.name = focusguard
package.domain = org.imosh

source.dir = .
source.include_exts = py,kv,png,jpg

version = 0.1

requirements = python3,kivy,plyer

orientation = portrait

fullscreen = 1

android.permissions = VIBRATE,POST_NOTIFICATIONS

android.api = 33
android.minapi = 21
android.ndk = 25b

android.accept_sdk_license = True

[buildozer]

log_level = 2
warn_on_root = 1