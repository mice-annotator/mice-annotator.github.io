#!/usr/bin/python
from boto.mturk.connection import MTurkConnection
from boto.mturk.question import ExternalQuestion
import boto.mturk.qualification as mtqu
from dateutil.parser import *

ACCESS_ID = 'AKIAILGF6HPJT2JFNJUA'
SECRET_KEY = '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'
HOST = 'mechanicalturk.sandbox.amazonaws.com' # Use this to post to the sandbox instead
# HOST = 'mechanicalturk.amazonaws.com'

def PostHits():
  mtc = MTurkConnection(aws_access_key_id=ACCESS_ID,
                        aws_secret_access_key=SECRET_KEY,
                        host=HOST)
  
  
  # q = ExternalQuestion(external_url = "https://timbrady.org/turk/monthnumber/", frame_height=675)
  q = ExternalQuestion(external_url = "https://github.com/mice-annotator/mice-annotator.github.io", frame_height=675)
  keywords = ['mice','bounding box']
  title = 'I love mice so much!'
  experimentName = "mice_bounding_box"
  description = 'Draw bounding box for mice in the frame.'
  pay = 0.02
  
  qualifications = mtqu.Qualifications()
  qualifications.add(mtqu.PercentAssignmentsApprovedRequirement('GreaterThanOrEqualTo', 90))
  qualifications.add(mtqu.LocaleRequirement("EqualTo", "US"))
  #qualifications.add(mtqu.Requirement("2Z046OQ1SNQQREGXAFSQPCNR1605PN"))

  theHIT = mtc.create_hit(question=q,
                          lifetime=10 * 60 * 60, # 10 hours
                          max_assignments=3,
                          title=title,
                          description=description,
                          keywords=keywords,
                          qualifications=qualifications,
                          reward=pay,
                          duration=120 * 60, # 120 minutes
                          approval_delay=5 * 60 * 60, # 5 hours
                          annotation=experimentName)

  assert(theHIT.status == True)
  print(theHIT)
  print(theHIT[0].HITId)

PostHits()
