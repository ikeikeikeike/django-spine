class {{ app_class.title }} extends Spine.Controller
  constructor: ->
    super

    # Initialize controllers:
    #  @append(@items = new {{ app_class }}.Items)
    #  ...

    Spine.Route.setup()

window.{{ app_class.title }} = {{ app_class.title }}