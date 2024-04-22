import pusher

pusher_client = pusher.Pusher(
  app_id='1792100',
  key='1a440f149aaf7396c997',
  secret='4d2acd37b5db3c0a08b8',
  cluster='mt1',
  ssl=False
)

pusher_client.trigger('my-channel', 'my-event', {'message': 'hello world'})
