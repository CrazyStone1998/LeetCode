select FirstName, LastName, City, State
    from Person left join Address
    where Person.PersonId = Address.PersonId