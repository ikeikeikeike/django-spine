class {{ app_class.title }}.{{ class_name.title }} extends Spine.Model
  @configure '{{ class_name.title }}', '{{ fields|join:"', '" }}'
  @extend Spine.Model.Ajax
  @url: "/{{ app_class }}/{{ class_name.pluralize }}"