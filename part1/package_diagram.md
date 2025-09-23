classDiagram
    class PresentationLayer {
        <<Package>>
        +UserService
        +PlaceService
        +APIEndpoints
    }
    class BusinessLogicLayer {
        <<Package>>
        +User
        +Place
        +Review
        +Amenity
    }
    class PersistenceLayer {
        <<Package>>
        +Database
        +Repository
    }
    
    PresentationLayer --> BusinessLogicLayer : Utilise via Facade
    BusinessLogicLayer --> PersistenceLayer : Persiste les données
