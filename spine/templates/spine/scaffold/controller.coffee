$ = jQuery.sub()
{{ class_name.title }} = {{ app_class.title }}.{{ class_name.title }}

$.fn.item = ->
  elementID   = $(@).data('id')
  elementID or= $(@).parents('[data-id]').data('id')
  {{ class_name.title }}.find(elementID)

class New extends Spine.Controller
  events:
    'click [data-type=back]': 'back'
    'submit form': 'submit'

  constructor: ->
    super
    @active @render

  render: ->
    @html @view('{{ class_name.pluralize }}/new')

  back: ->
    @navigate '/{{ class_name.pluralize }}'

  submit: (e) ->
    e.preventDefault()
    {{ class_name }} = {{ class_name.title }}.fromForm(e.target).save()
    @navigate '/{{ class_name.pluralize }}', {{ class_name }}.id if {{ class_name }}

class Edit extends Spine.Controller
  events:
    'click [data-type=back]': 'back'
    'submit form': 'submit'

  constructor: ->
    super
    @active (params) ->
      @change(params.id)

  change: (id) ->
    @item = {{ class_name.title }}.find(id)
    @render()

  render: ->
    @html @view('{{ class_name.pluralize }}/edit')(@item)

  back: ->
    @navigate '/{{ class_name.pluralize }}'

  submit: (e) ->
    e.preventDefault()
    @item.fromForm(e.target).save()
    @navigate '/{{ class_name.pluralize }}'

class Show extends Spine.Controller
  events:
    'click [data-type=edit]': 'edit'
    'click [data-type=back]': 'back'

  constructor: ->
    super
    @active (params) ->
      @change(params.id)

  change: (id) ->
    @item = {{ class_name.title }}.find(id)
    @render()

  render: ->
    @html @view('{{ class_name.pluralize }}/show')(@item)

  edit: ->
    @navigate '/{{ class_name.pluralize }}', @item.id, 'edit'

  back: ->
    @navigate '/{{ class_name.pluralize }}'

class Index extends Spine.Controller
  events:
    'click [data-type=edit]':    'edit'
    'click [data-type=destroy]': 'destroy'
    'click [data-type=show]':    'show'
    'click [data-type=new]':     'new'

  constructor: ->
    super
    {{ class_name.title }}.bind 'refresh change', @render
    {{ class_name.title }}.fetch()

  render: =>
    {{ class_name.pluralize }} = {{ class_name.title }}.all()
    @html @view('{{ class_name.pluralize }}/index')({{ class_name.pluralize }}: {{ class_name.pluralize }})

  edit: (e) ->
    item = $(e.target).item()
    @navigate '/{{ class_name.pluralize }}', item.id, 'edit'

  destroy: (e) ->
    item = $(e.target).item()
    item.destroy() if confirm('Sure?')

  show: (e) ->
    item = $(e.target).item()
    @navigate '/{{ class_name.pluralize }}', item.id

  new: ->
    @navigate '/{{ class_name.pluralize }}/new'

class {{ app_class.title }}.{{ class_name.pluralize.title }} extends Spine.Stack
  controllers:
    index: Index
    edit:  Edit
    show:  Show
    new:   New

  routes:
    '/{{ class_name.pluralize }}/new':      'new'
    '/{{ class_name.pluralize }}/:id/edit': 'edit'
    '/{{ class_name.pluralize }}/:id':      'show'
    '/{{ class_name.pluralize }}':          'index'

  default: 'index'
  className: 'stack {{ class_name.pluralize }}'