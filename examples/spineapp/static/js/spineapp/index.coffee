class Spineapp extends Spine.Controller
  constructor: ->
    super

    # Initialize controllers:
    #  @append(@items = new spineapp.Items)
    #  ...

    @append(@examples = new Spineapp.Examples)

    Spine.Route.setup()

window.Spineapp = Spineapp