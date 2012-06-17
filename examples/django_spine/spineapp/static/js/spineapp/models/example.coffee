class Spineapp.Example extends Spine.Model
  @configure 'Example', 'name', 'content', 'message'
  @extend Spine.Model.Ajax
  @url: "/spineapp/examples"