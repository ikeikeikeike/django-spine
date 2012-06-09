class {{ app_class.title }}.{{ class_name.title }} extends Spine.Model
  @configure '{{ class_name.title }}', '{{ fields|join:"', '" }}'
  @extend Spine.Model.Ajax