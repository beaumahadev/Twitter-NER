#!/usr/bin/python

import sys
import os

os.system("java -Xmx1024m -cp /homes/gws/aritter/mallet-2.0.6/lib/mallet-deps.jar:/homes/gws/aritter/mallet-2.0.6/dist/mallet.jar cc.mallet.fst.SimpleTagger --include-input true --test seg=B-ENTITY.I-ENTITY --model-file %s %s" % (sys.argv[1], sys.argv[2]))

#os.system("java -Xmx1024m -cp /homes/gws/aritter/mallet-2.0.6/lib/mallet-deps.jar:/homes/gws/aritter/mallet-2.0.6/dist/mallet.jar cc.mallet.fst.SimpleTagger --include-input true --test seg=B-ENTITY.I-ENTITY,B-ORGANIZATION.I-ORGANIZATION,B-LOCATION.I-LOCATION,B-PERSON.I-PERSON,B-EVENT.I-EVENT,B-OTHER.I-OTHER --model-file %s %s" % (sys.argv[1], sys.argv[2]))

#os.system("java -Xmx1024m -cp /homes/gws/aritter/mallet-2.0.6/lib/mallet-deps.jar:/homes/gws/aritter/mallet-2.0.6/dist/mallet.jar cc.mallet.fst.SimpleTagger --include-input true --test seg=B-LOCATION.I-LOCATION,B-PERSON.I-PERSON,B-OTHER.I-OTHER --model-file %s %s" % (sys.argv[1], sys.argv[2]))

#os.system("java -Xmx1024m -cp /homes/gws/aritter/mallet-2.0.6/lib/mallet-deps.jar:/homes/gws/aritter/mallet-2.0.6/dist/mallet.jar cc.mallet.fst.SimpleTagger --include-input true --test seg=B-loc.I-loc,B-per.I-per,B-org.I-org,B-event.I-event,B-company.I-company,B-product.I-product,B-internetwebsite.I-internetwebsite,B-musicartist.I-musicartist,B-venue.I-venue,B-film.I-film,B-tvshow.I-tvshow,B-sportsteam.I-sportsteam,B-other.I-other --model-file %s %s" % (sys.argv[1], sys.argv[2]))
