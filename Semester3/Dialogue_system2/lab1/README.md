
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
