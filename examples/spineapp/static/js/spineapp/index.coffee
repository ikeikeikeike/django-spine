class Spineapp extends Spine.Controller
  constructor: ->
    super

    # Initialize controllers:
    #  @append(@items = new spineapp.Items)
    #  ...

    Spine.Route.setup()

window.Spineapp = Spineapp