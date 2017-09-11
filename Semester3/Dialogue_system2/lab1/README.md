
s-hum-g212-m09:HelloWorldLab1_2017_test2 gusyansu$ tdm build
Building generated grammar for DDD u'hello_world'.
[eng] Cleaning build directory u'build/eng'...Done.
[eng] Generating grammar.
Missing grammar entry: How do the speakers talk about the issue alarm_off? The entry is used in questions such as "Do you want to know X?" or "I want to know X", where X is the grammar entry.

Example:

  <question speaker="all" predicate="alarm_off" type="wh_question">alarm off</question>

Alternatively, you can specify several possible utterances in a list:

  <question speaker="all" predicate="alarm_off" type="wh_question">
    <one-of>
      <item>alarm off one way</item>
      <item>alarm off another way</item>
    </one-of>
  </question>



[eng] Asserting that language grammar is lower case...Done.
[eng] Finished generating grammar.
[eng] Building generated grammar.
[eng] Finished building generated grammar.
[eng] Not using word list correction, will not generate word list.
[eng] No ASR specified, will not build language model.
Finished building generated grammar for DDD u'hello_world'.
s-hum-g212-m09:HelloWorldLab1_2017_test2 gusyansu$ tdm run eng
Accepting connections on ws://localhost:9090/websocket
S> Do you want to know the current time or set the time?

what time is it
S> 00:00.

set time to eleven thrirty
S> Returning to the start view. Do you want to know the current time or set the time?

S> Do you want to set the time, set the alarm, [set_time_oneshot] or [set_alarm_oneshot]?

set time to eleven nine
S> So, Do you want to know the current time or set the time?

S> Do you want to set the time, set the alarm, [set_time_oneshot] or [set_alarm_oneshot]?

set the time to eleven nine
S> So, Do you want to know the current time or set the time?

S> The time was set to 11: 9 by oneshot.

what time is it
S> Returning to the start view. So, Do you want to know the current time or set the time?

S> 11:09.

set alarm to nine thirty
S> Returning to the start view. Do you want to know the current time or set the time?

S> The alarm was set to 9: 30 by oneshot.

is alarm on
S> Returning to the start view. So, Do you want to know the current time or set the time?

S> True.

alarm off
S> Returning to the start view. So, Do you want to know the current time or set the time?

S> Alarm is off now..

is alarm off
S> Returning to the start view. So, Do you want to know the current time or set the time?

S> Alarm is already off..

is alarm on
S> Returning to the start view. So, Do you want to know the current time or set the time?

S> False.

alarm off
S> Returning to the start view. So, Do you want to know the current time or set the time?

S> Alarm is already off..

^CShutting down, hang on...
s-hum-g212-m09:HelloWorldLab1_2017_test2 gusyansu$ tdm run eng
Accepting connections on ws://localhost:9090/websocket
S> Do you want to know the current time or set the time?

set the alarm
S> What hour?

one
S> What minute?

two
S> The alarm was set to 1: 2.

set the alarm to nine thirty
S> Returning to the start view. Do you want to know the current time or set the time?

S> The alarm was set to 9: 30 by oneshot.

set the time to seven ten
S> Returning to the start view. So, Do you want to know the current time or set the time?

S> The time was set to 7: 10 by oneshot.

is alarm on
S> Returning to the start view. So, Do you want to know the current time or set the time?

S> True.

alarm off
S> Returning to the start view. So, Do you want to know the current time or set the time?

S> Alarm is off now..

is alarm on
S> Returning to the start view. So, Do you want to know the current time or set the time?

S> False.

alarm off
S> Returning to the start view. So, Do you want to know the current time or set the time?

S> Alarm is already off..


