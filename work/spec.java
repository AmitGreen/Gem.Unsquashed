//  Specification for Gem

interface TreeNode {                                                    //  A node of JSON object
    public boolean                      is_boolean();                   //  True for JSON boolean
    public boolean                      is_double();                    //  True for JSON number that has a '.', 'e', or 'E' in it
    public boolean                      is_integer();                   //  True for JSON number that does not have a '.', 'e', or 'E' in it.
    public boolean                      is_map();                       //  True for JSON object
    public boolean                      is_none();                      //  True for JSON null
    public boolean                      is_number();                    //  True for JSON number
    public boolean                      is_string();                    //  True for JSON string
    public boolean                      is_tuple();                     //  True for JSON array
    

    //
    //  The following functions treat the tree_node, as the expected type (i.e.: "cast"):
    //
    //      The function name indicates what to do if the actual tree node is not the expected type:
    //
    //      1.  Return a specific value; OR
    //      2.  Throw an exception
    //
    //  NOTE:
    //      Map's & Tuple's do not have a "*_or_other" method on purpose.
    //
    public Gem_Boolean                  boolean(Box x)                          //  Return Gem_Boolean, or throw an exception
    public Gem_Boolean                  boolean_OR_false();                     //  Return Gem_Boolean, or `gem_false`
    public Gem_Boolean                  boolean_OR_other(Gem_Boolean v);        //  Return Gem_Boolean, or `v`
    public Gem_Boolean                  boolean_OR_TRUE();                      //  Return Gem_Boolean, or `gem_true`

    public Gem_Boolean_0                boolean_0(Box x);                       //  Return Gem_Boolean_0, or throw an exception
    public Gem_Boolean_0                boolean_0__OR__false();                 //  Return Gem_Boolean_0, or `gem_false`
    public Gem_Boolean_0                boolean_0__OR__none();                  //  Return Gem_Boolean_0, or `gem_boolean_none`
    public Gem_Boolean_0                boolean_0__OR__other(Gem_Boolean_0 v);  //  Return Gem_Boolean_0, or `v`
    public Gem_Boolean_0                boolean_0__OR__TRUE();                  //  Return Gem_Boolean_0, or `gem_true`

    public Gem_Double                   double(Box x);                          //  Return Gem_Double, or throw an exception
    public Gem_Double                   double_OR_other(Gem_Double v);          //  Return Gem_Double, or `v`
    public Gem_Double                   double_OR_zero();                       //  Return Gem_Double, or `gem_double_0_0`

    public Gem_Double_0                 double_0(Box x);                        //  Return Gem_Double_0, or throw an exception
    public Gem_Double_0                 double_0__OR__none();                   //  Return Gem_Double_0, or `gem_double_none`
    public Gem_Double_0                 double_0__OR__other(Gem_Double_0 v);    //  Return Gem_Double_0, or `v`
    public Gem_Double_0                 double_0__OR__zero();                   //  Return Gem_Double_0, or `gem_double_0_0`

    public Gem_Integer                  integer(Box x);                         //  Return Gem_Integer, or throw an exception
    public Gem_Integer                  integer_OR_other(Gem_Integer v);        //  Return Gem_Integer, or `v`
    public Gem_Integer                  integer_OR_zero();                      //  Return Gem_Integer, or `gem_integer_0`

    public Gem_Integer_0                integer_0(Box x);                       //  Return Gem_Integer_0, or throw an exception
    public Gem_Integer_0                integer_0__OR__none();                  //  Return Gem_Integer_0, or `gem_integer_none`
    public Gem_Integer_0                integer_0__OR__other(Gem_Integer_0 v);  //  Return Gem_Integer_0, or `v`
    public Gem_Integer_0                integer_0__OR__zero();                  //  Return Gem_Integer_0, or `gem_integer_0_0`

    public Gem_TreeNodeMap              map(Box x);                             //  Return Gem_TreeNodeMap, or throw an exception
    public Gem_TreeNodeMap              map_OR_empty();                         //  Return Gem_TreeNodeMap, or `gem_tree_node_map_empty`

    public Gem_TreeNodeMap_0            map_0(Box x);                           //  Return Gem_TreeNodeMap_0, or throw an exception
    public Gem_TreeNodeMap_0            map_0__OR__empty();                     //  Return Gem_TreeNodeMap_0, or `gem_tree_node_map_empty`
    public Gem_TreeNodeMap_0            map_0__OR__none();                      //  Return Gem_TreeNodeMap_0, or `gem_tree_node_map_none`

    public Gem_String                   string(Box x);                          //  Return Gem_String, or throw an exception
    public Gem_String                   string_OR_empty();                      //  Return Gem_String, or `gem_string_empty`
    public Gem_String                   string_OR_other(Gem_String s);          //  Return Gem_String, or `s`

    public Gem_String_0                 string_0(Box x);                        //  Return Gem_String_0, or throw an exception
    public Gem_String_0                 string_0__OR__empty();                  //  Return Gem_String_0, or `gem_string_empty`
    public Gem_String_0                 string_0__OR__none();                   //  Return Gem_String_0, or `gem_string_none`
    public Gem_String_0                 string_0__OR__other(Gem_String_0 s);    //  Return Gem_String_0, or `s`

    public Gem_TreeNodeTuple            tuple(Box x);                           //  Return Gem_TreeNodeTuple, or throw an exception
    public Gem_TreeNodeTuple            tuple_OR_empty();                       //  Return Gem_TreeNodeTuple, or `gem_tree_node_tuple_empty`

    public Gem_TreeNodeTuple_0          tuple_0(Box x);                         //  Return Gem_TreeNodeTuple_0, or throw an exception
    public Gem_TreeNodeTuple_0          tuple_0__OR__empty();                   //  Return Gem_TreeNodeTuple_0, or `gem_tree_node_tuple_empty`
    public Gem_TreeNodeTuple_0          tuple_0__OR__none();                    //  Return Gem_TreeNodeTuple_0, or `gem_tree_node_tuple_none`


    //
    //  The following functions treat the tree_node, as a tuple with an expected type at the `index` (i.e.: "cast"):
    //
    //      The function name indicates what to do if the actual tree node is not a tuple, or the the expected type is not at the index:
    //
    //      1.  Return a specific value; OR
    //      2.  Throw an exception
    //
    //  NOTE:
    //      Map's & Tuple's do not have a "*_or_other" method on purpose.
    //
    public Gem_Boolean                  index_boolean(int index, Box x);
    public Gem_Boolean                  index_boolean_OR_false(int index);
    public Gem_Boolean                  index_boolean_OR_other(int index, Gem_Boolean v);
    public Gem_Boolean                  index_boolean_OR_TRUE(int index);

    public Gem_Boolean_0                index__boolean_0(int index, Box x);
    public Gem_Boolean_0                index__boolean_0__OR__false(int index);
    public Gem_Boolean_0                index__boolean_0__OR__none(int index);
    public Gem_Boolean_0                index__boolean_0__OR__other(int index, Gem_Boolean_0 v);
    public Gem_Boolean_0                index__boolean_0__OR__TRUE(int index);

    public Gem_Double                   index_double(int index, Box x);
    public Gem_Double                   index_double_OR_other(int index, Gem_Double v);
    public Gem_Double                   index_double_OR_zero(int index);

    public Gem_Double_0                 index__double_0(int index, Box x);
    public Gem_Double_0                 index__double_0__OR__none(int index);
    public Gem_Double_0                 index__double_0__OR__other(int index, Gem_Double_0 v);
    public Gem_Double_0                 index__double_0__OR__zero(int index);

    public Gem_Integer                  index__integer(int index, Box x);
    public Gem_Integer                  index__integer_OR_other(int index, Gem_Integer v);
    public Gem_Integer                  index__integer_OR_zero(int index);

    public Gem_Integer_0                index__integer_0(int index, Box x);
    public Gem_Integer_0                index__integer_0__OR__none(int index);
    public Gem_Integer_0                index__integer_0__OR__other(int index, Gem_Integer_0 v);
    public Gem_Integer_0                index__integer_0__OR__zero(int index);

    public Gem_TreeNodeMap              index_map(int index, Box x);
    public Gem_TreeNodeMap              index_map_OR_empty(int index);

    public Gem_TreeNodeMap_0            index__map_0(int index, Box x);
    public Gem_TreeNodeMap_0            index__map_0__OR__empty(int index);
    public Gem_TreeNodeMap_0            index__map_0__OR__none(int index);

    public Gem_String                   index_string(int index, Box x);
    public Gem_String                   index_string_OR_empty(int index);
    public Gem_String                   index_string_OR_other(int index, Gem_String s);

    public Gem_String_0                 index__string_0(int index, Box x);
    public Gem_String_0                 index__string_0__OR__empty(int index);
    public Gem_String_0                 index__string_0__OR__none(int index);
    public Gem_String_0                 index__string_0__OR__other(int index, Gem_String_0 s);

    public Gem_TreeNodeTuple            index_tuple(int index, Box x);
    public Gem_TreeNodeTuple            index_tuple_OR_empty(int index);

    public Gem_TreeNodeTuple_0          index__tuple_0(int index, Box x);
    public Gem_TreeNodeTuple_0          index__tuple_0__OR__empty(int index);
    public Gem_TreeNodeTuple_0          index__tuple_0__OR__none(int index);
}
