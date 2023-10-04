const app = Vue.createApp({
  data: () => ({
    newItem: '',
    todos: []
  }),
  methods: {
    // タスクリストにタスクを追加する
    addItem: function(event) {
      if(this.newItem === '') return
      let todo = {
        item: this.newItem,
        isDone: false
      }
      this.todos.push(todo)
      this.newItem = ''
      console.log(event)
    },
    // タスクリストからタスクを削除する
    deleteItem: function(index){
      this.todos.splice(index, 1)
    }
  }
})
app.mount('#app')