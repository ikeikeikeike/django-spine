$ = jQuery.sub()
Example = Spineapp.Example

$.fn.item = ->
  elementID   = $(@).data('id')
  elementID or= $(@).parents('[data-id]').data('id')
  Example.find(elementID)

class New extends Spine.Controller
  events:
    'click [data-type=back]': 'back'
    'submit form': 'submit'

  constructor: ->
    super
    @active @render

  render: ->
    @html @view('examples/new')

  back: ->
    @navigate '/examples'

  submit: (e) ->
    e.preventDefault()
    example = Example.fromForm(e.target).save()
    @navigate '/examples', example.id if example

class Edit extends Spine.Controller
  events:
    'click [data-type=back]': 'back'
    'submit form': 'submit'

  constructor: ->
    super
    @active (params) ->
      @change(params.id)

  change: (id) ->
    @item = Example.find(id)
    @render()

  render: ->
    @html @view('examples/edit')(@item)

  back: ->
    @navigate '/examples'

  submit: (e) ->
    e.preventDefault()
    @item.fromForm(e.target).save()
    @navigate '/examples'

class Show extends Spine.Controller
  events:
    'click [data-type=edit]': 'edit'
    'click [data-type=back]': 'back'

  constructor: ->
    super
    @active (params) ->
      @change(params.id)

  change: (id) ->
    @item = Example.find(id)
    @render()

  render: ->
    @html @view('examples/show')(@item)

  edit: ->
    @navigate '/examples', @item.id, 'edit'

  back: ->
    @navigate '/examples'

class Index extends Spine.Controller
  events:
    'click [data-type=edit]':    'edit'
    'click [data-type=destroy]': 'destroy'
    'click [data-type=show]':    'show'
    'click [data-type=new]':     'new'

  constructor: ->
    super
    Example.bind 'refresh change', @render
    Example.fetch()

  render: =>
    examples = Example.all()
    @html @view('examples/index')(examples: examples)

  edit: (e) ->
    item = $(e.target).item()
    @navigate '/examples', item.id, 'edit'

  destroy: (e) ->
    item = $(e.target).item()
    item.destroy() if confirm('Sure?')

  show: (e) ->
    item = $(e.target).item()
    @navigate '/examples', item.id

  new: ->
    @navigate '/examples/new'

class Spineapp.Examples extends Spine.Stack
  controllers:
    index: Index
    edit:  Edit
    show:  Show
    new:   New

  routes:
    '/examples/new':      'new'
    '/examples/:id/edit': 'edit'
    '/examples/:id':      'show'
    '/examples':          'index'

  default: 'index'
  className: 'stack examples'