#!/usr/bin/python

import sys, optparse

try:
    import gconf
except:
    print  'You need to install the python bindings for gconf'
    sys.exit(1)

LUCID = "menu,maximize,minimize,close:"
RHS = "menu:minimize,maximize,close"


KEY = "/apps/metacity/general/button_layout"

class OptionParser (optparse.OptionParser):

    def check_required (self, opt):
      option = self.get_option(opt)

      # Assumes the option's 'default' is set to None!
      if getattr(self.values, option.dest) is None:
          self.error("%s option not supplied" % option)


usage = "usage: %prog [options] arg"
parser = OptionParser(usage)
parser.add_option("-d", "--default", action="store_true", dest="restore_default", default=False, help = "Restore Lucid defaults.")
parser.add_option("-r", "--right", action="store_true", dest="position_right", default=False, help = "Position window controls to the right.")

(options, args) = parser.parse_args()

gconf_client = gconf.client_get_default()

if (options.restore_default):
    print "Restoring default options."
    gconf_client.set_string(KEY, LUCID)
elif (options.position_right):
    print "Setting controls to right of window border."
    gconf_client.set_string(KEY, RHS)
else:
    parser.print_help()
    sys.exit(1)



